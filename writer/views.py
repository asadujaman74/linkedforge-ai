from django.shortcuts import render , redirect

# Create your views here.

from .forms import PostForm
from .services import generate_post
from .models import PostHistory


def home(request):
    form = PostForm()
    output = request.session.pop('generated_output', None)

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            thought = form.cleaned_data['thought']
            tone = form.cleaned_data['tone']
            audience = form.cleaned_data['audience']

            # AI generate
            output = generate_post(thought, tone, audience)

            # save history
            PostHistory.objects.create(
                raw_thought=thought,
                tone=tone,
                audience=audience,
                generated_post=output
            )

            request.session['generated_output'] = output
            return redirect('home')

    return render(request, 'writer/home.html', {
        'form': form,
        'output': output,
    })


def history(request):
    # keep only latest 5 in database
    extra_posts = PostHistory.objects.order_by('-created_at')[5:]
    if extra_posts:
        PostHistory.objects.filter(id__in=[p.id for p in extra_posts]).delete()

    posts = PostHistory.objects.order_by('-created_at')[:5]
    return render(request, 'writer/history.html', {'posts': posts})

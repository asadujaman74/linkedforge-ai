from django.shortcuts import render , redirect

# Create your views here.

from .forms import PostForm
from .services import generate_post
from .models import PostHistory


def index(request):
    return render(request, 'writer/home.html')

def home(request):
    form = PostForm()
    output = request.session.pop('generated_output', None)

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            thought = form.cleaned_data['thought']
            tone = form.cleaned_data['tone']
            audience = form.cleaned_data['audience']

            try:
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

            except Exception as e:
                print("GENERATE ERROR:", e)
                output = "Something went wrong while generating post 😅"

    return render(request, 'writer/generate_post.html', {
        'form': form,
        'output': output,
    })

def history(request):
    try:
        posts = PostHistory.objects.order_by('-created_at')[:5]
    except Exception as e:
        print("HISTORY ERROR:", e)
        posts = []

    return render(request, 'writer/history.html', {
        'posts': posts
    })

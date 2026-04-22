from django import forms

class PostForm(forms.Form):

    TONE_CHOICES = [
        ('', 'Select Tone'),
        ('Professional', 'Professional'),
        ('Storytelling', 'Storytelling'),
        ('Friendly', 'Friendly'),
        ('Technical', 'Technical'),
        ('Motivational', 'Motivational'),
    ]

    AUDIENCE_CHOICES = [
        ('', 'Select Audience'),
        ('Recruiters', 'Recruiters'),
        ('Developers', 'Developers'),
        ('Founders', 'Founders'),
        ('Freelancers', 'Freelancers'),
        ('Students', 'Students'),
    ]

    thought = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Write your raw thought...'
        })
    )

    tone = forms.ChoiceField(
        choices=TONE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    audience = forms.ChoiceField(
        choices=AUDIENCE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
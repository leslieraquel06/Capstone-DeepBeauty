from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['names', 'content']

class SkincareQuizForm(forms.Form):
    EXPERIENCE_CHOICES = (
        ('a', 'Beginner'),
        ('b', 'Intermediate'),
        ('c', 'Advanced'),
    )
    TIME_CHOICES = (
        ('a', '5 minutes or less'),
        ('b', '10-15 minutes'),
        ('c', '20 minutes or more'),
    )
    SKINTYPE_CHOICES = (
        ('a', 'Dry'),
        ('b', 'Oily'),
        ('c', 'Normal'),
    )
    
    experience = forms.ChoiceField(label="How experienced are you with skincare?", choices=EXPERIENCE_CHOICES, widget=forms.RadioSelect)
    time = forms.ChoiceField(label="How much time do you have for your skincare routine?", choices=TIME_CHOICES, widget=forms.RadioSelect)
    skintype = forms.ChoiceField(label="What is your skin type?", choices=SKINTYPE_CHOICES, widget=forms.RadioSelect)
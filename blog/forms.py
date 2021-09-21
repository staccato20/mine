from django import forms
from django.db import models
from django.forms import fields, ModelForm, DateInput
from .models import Blog, Comment, Hashtag, Event

class CreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'writer', 'content', 'image', 'hashtags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']

#다이어리
class EventForm(ModelForm):
    class Meta:
        model = Event
        widgets = {
            'diary_start_time': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'diary_end_time': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['diary_start_time'].input_formats = ('%Y-%m-%d',)
        self.fields['diary_end_time'].input_formats = ('%Y-%m-%d',)
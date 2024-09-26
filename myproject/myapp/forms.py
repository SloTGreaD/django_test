from django import forms
from .models import BlogPost

class BlogPostForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=200)
    content = forms.CharField(widget=forms.Textarea, label='Содержимое')

class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
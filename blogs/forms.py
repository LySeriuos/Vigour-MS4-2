from django import forms
from .models import Blogs

from django import forms


class BlogForm(forms.ModelForm):
    class Meta:       
        model = Blogs
        fields = (
                  'title',
                  'content',)

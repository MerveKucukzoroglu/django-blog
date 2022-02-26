"""forms python file"""
from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """comments form"""
    class Meta:
        """Meta class"""
        model = Comment
        fields = ('body',)

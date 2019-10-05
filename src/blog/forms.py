from django import forms
from django.contrib.auth.models import User
from blog.models import Post, Comment, Reaction

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'post_title',
            'post_image',
            'post_description',
            'publish_status'
        ]

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'post_title',
            'post_image',
            'post_description',
            'publish_status'
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment_text'
        ]

class ReactForm(forms.ModelForm):
    class Meta:
        model = Reaction
        fields =[
            'react'
        ]
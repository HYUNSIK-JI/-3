from ftplib import error_perm
from django import forms
from .models import Review,Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content','grade']
        labels = {
            "title": "제목",
            "content": "내용",
            "grade":"평점",
        }
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields=['content',]
        labels = {
            "content": "",
        }
        error_messages = {
            'content': {
                'required':"",
            },
        }
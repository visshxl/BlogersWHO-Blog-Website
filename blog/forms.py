from django import forms

from .models import comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = comments
        exclude = ["post", "date"] #we dont want user to set the post by himself so we exc it
        labels = {
            "user_name": "Your Name",
            "email": "Your Email",
            "text": "Comment"
        }
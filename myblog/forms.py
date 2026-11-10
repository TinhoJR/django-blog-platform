from django import forms
from .models import Post,Comment



class PostForm(forms.ModelForm):
    
    class Meta :
        model = Post
        fields = ["title","author","body"]
        # exclude = []


    def clean_title(self):
        title = self.cleaned_data.get("title") 
        if len(title) < 5:
            raise forms.ValidationError("Title must be at leats 5 characters long") 

        return title  


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["comment"]
        # exclude = ["user","post","is_deleted","image","last_modified","date"]  
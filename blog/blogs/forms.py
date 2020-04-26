from django import forms

from blogs.models import BlogPost

class BlogPostForm(forms.ModelForm):
    """define the form fields"""
    class Meta:
        model = BlogPost
        fields = ['title','text','is_public']
        labels = {'title': '','text':'','is_public':'public post?'}
        widgets ={'text':forms.Textarea(attrs={'cols':80}),'is_public':forms.CheckboxInput,check_test=False}
        


from django import forms

from blogs.models import BlogPost

class BlogPostForm(forms.ModelForm):
    """define the form fields"""
    class Meta:
        model = BlogPost
        fields = ['title','text']
        labels = {'title': '','text':''}
        widgets ={'text':forms.Textarea(attrs={'cols':80})}
        


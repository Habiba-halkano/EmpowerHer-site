from .models import Reports, Post, Comments, Contact, Reply
from django import forms
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Share something...'}),
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your reply here...'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'

class ReportForm(forms.ModelForm):
    class Meta:
        model = Reports
        fields = ['title', 'location', 'description', 'supporting_files', 'date']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',  # HTML5 Date Picker
                'class': 'form-control',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the report title'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the location'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Describe the issue in detail'
            }),
            'supporting_files': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 5}),
        }

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
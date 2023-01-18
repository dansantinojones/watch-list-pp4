from .models import Comment
from django import forms
from cloudinary.models import CloudinaryField


class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ('body',)


class AddMedia(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    platform = forms.CharField(max_length=20)
    genre = forms.CharField(max_length=20)
    type = forms.CharField(max_length=20)
    media_image = CloudinaryField('image', default='placeholder')

    def send_recommendation(self):
        pass
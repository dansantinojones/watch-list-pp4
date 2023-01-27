from .models import Comment, Media, RecommendBox
from django import forms
from cloudinary.models import CloudinaryField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CreateMedia(forms.ModelForm):
    class Meta:
        model = Media
        fields = (
            'title', 'description', 'platform', 'genre', 'type', 'media_image'
            )

    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    platform = forms.CharField(max_length=20)
    genre = forms.CharField(max_length=20)
    type = forms.CharField(max_length=20)
    media_image = CloudinaryField('image', default='placeholder')

    def send_recommendation(self):
        pass


class UpdateMedia(forms.ModelForm):
    class Meta:
        model = Media
        fields = (
            'title', 'description', 'platform', 'genre', 'type', 'media_image'
            )

    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    platform = forms.CharField(max_length=20)
    genre = forms.CharField(max_length=20)
    type = forms.CharField(max_length=20)
    media_image = CloudinaryField('image', default='placeholder')

    def send_recommendation(self):
        pass


class DeleteMedia(forms.ModelForm):
    class Meta:
        model = Media
        fields = ()

    def send_recommendation(self):
        pass


class RecommendBoxForm(forms.ModelForm):
    class Meta:
        model = RecommendBox
        fields = ('title',)

    title = forms.CharField(max_length=50)

    def send_recommendation(self):
        pass

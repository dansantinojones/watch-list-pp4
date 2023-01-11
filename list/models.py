from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Watch"), (1, "Watched"))


class Media(models.Model):
    title = models.CharField(max_length=50, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    platform = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    media_image = CloudinaryField('image', default='placeholder')
    recommended = models.ManyToManyField(User, related_name='recommend', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
        return self.platform
        return self.genre
        return self.type

    def number_of_recommended(self):
        return self.recommended.count()


class Comment(models.Model):
    media = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

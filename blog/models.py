from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import datetime


STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class CallBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=50, null=False, blank=False)
    client_email = models.EmailField(null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    details = models.TextField(blank=True)
    call_date = models.DateField(null=False, blank=False)
    call_time = models.TimeField(null=True, blank=False)
    
    def get_client_name(self):
        return self.client_name

    def get_client_email(self):
        return self.client_email

    def get_phone_number(self):
        return self.phone_number

    def call_data(self):
        return f" {self.call_date} at {self.call_time}"
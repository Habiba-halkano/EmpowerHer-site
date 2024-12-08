from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# Create your models here.
#model resources
class Resources(models.Model):
    Resource_choices = [
        ('article', 'Article'),
        ('video', 'Video'),
        ('infographics', 'Infographics')
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    resource_type = models.CharField(max_length=100, choices=Resource_choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def short_content(self):
        content_text = str(self.content)  # Ensure content is a string
        return content_text[:500] + "..." if len(content_text) > 500 else content_text


class SupportGroups(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    contact_info = models.TextField()
    location = models.TextField()
    services = models.TextField()

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_at = models.DateTimeField()

class Events(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.TextField()
    date = models.DateTimeField()

class Reports(models.Model):
    title = models.CharField(max_length=255, default="Untitled Report")
    location = models.CharField(max_length=255)
    description = models.TextField()
    supporting_files = models.FileField(upload_to='reports/files/', blank=True, null=True)
    date = models.DateField()

class Post(models.Model):
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name='posts',
            null=True,
            blank=True
        )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.username} - {self.content[:30]}"


class Reply(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='replies'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='replies'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.username} on Post {self.post.id}"


class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    SUBJECT_CHOICES = [
        ('support', 'support'),
        ('Feedback', 'Feedback'),
        ('inquiry', 'inquiry'),
        ('other', 'other')
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
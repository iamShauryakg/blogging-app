from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to="blog/media/", null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
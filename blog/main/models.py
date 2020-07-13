from django.db import models
from django.urls import reverse

class Posts(models.Model):
    post = models.TextField()
    post_description = models.TextField()
    post_title = models.CharField(max_length=90)

    class Meta:
        verbose_name_plural = "Posts"

    def get_absolute_url(self):
        return f"{self.id}/"
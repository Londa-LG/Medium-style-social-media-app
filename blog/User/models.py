from django.db import models

# Create your models here.
class Posts(models.Model):
    post = models.TextField()
    post_description = models.TextField()
    post_title = models.CharField(max_length=90)

    class Meta:
        verbose_name_plural = "Posts"
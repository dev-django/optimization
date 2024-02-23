from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'POST'
        ordering = ["-id"]
        verbose_name = "Post"
        verbose_name_plural = ""

from django.db import models
from django.contrib.auth.models import User


class PostTable(models.Model):
    post_desc = models.CharField(max_length=10024)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='availablepost')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.post_desc[:256]

class CommentTable(models.Model):
    comment_desc = models.CharField(max_length=10024)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="availablecommentuser")
    post_ref = models.ForeignKey(PostTable, on_delete=models.CASCADE, related_name='availablecomment')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    # class Meta:
    #     ordering = ['created']
    
    def __str__(self):
        return self.comment_desc[:50]
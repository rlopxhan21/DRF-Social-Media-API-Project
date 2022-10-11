from django.contrib import admin
from .models import PostTable, CommentTable

# Register your models here.

admin.site.register(PostTable)
admin.site.register(CommentTable)
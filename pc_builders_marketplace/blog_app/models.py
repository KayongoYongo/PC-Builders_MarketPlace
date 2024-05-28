from django.conf import settings
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = CKEditor5Field(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')])

    def __str__(self):
        return self.title   
from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')
    created_at = models.DateTimeField(auto_now_add=True)
    #username = models.CharField(max_length=50, null=False, blank=False)


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='Categories'
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='category_name_case_insensitive_unique',
                violation_error_message='Category already exists (case insensitive match)'
            ),
        ] 


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        # ordering
        ordering = ['-updated_at']


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_at']
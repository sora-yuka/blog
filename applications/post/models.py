from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.SlugField(primary_key=True)
    parent = models.ForeignKey('Category', 
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               related_query_name='children')
    
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE, 
                              related_name='Post')
    category = models.ForeignKey(Category, 
                                 on_delete=models.CASCADE,
                                 related_name='Post')
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    owner = models.ForeignKey(User, 
                              on_delete=models.SET_NULL,
                              related_name='comment',
                              null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comment')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.owner.username} {self.post.title}"
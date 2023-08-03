from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug          = models.SlugField(max_length=100,unique=True)
    description   = models.TextField(max_length=250, blank = True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get_url(self):
        return reverse('tools_by_category', args =[self.slug])
    def __str__(self):
        return self.category_name
    
    
    

class AiTool(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    link = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='AiTools')
    
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('tool_detail', args = [self.slug])
            
    def __str__(self):
        return self.name
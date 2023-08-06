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
        
    SearchableFields  = ['category_name']
        
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
    
    SearchableFields  = ['category__category_name', 'name',]
    def get_url(self):
        return reverse('tool_detail', args = [self.slug])
            
    def __str__(self):
        return self.name
    
    
class Contact(models.Model):
    customer_name     = models.CharField(max_length=50)
    customer_surname  = models.CharField(max_length=50)
    email             = models.EmailField(max_length=254)
    phone_number      = models.CharField(max_length=50)
    message           = models.TextField(max_length = 5000)
    is_reviewed       = models.BooleanField(default=False)
    is_entertained    = models.BooleanField(default=False)
    created_date      = models.DateTimeField(auto_now_add=True)
    modified_date     = models.DateTimeField(auto_now=True)
    SearchableFields  = ['customer_name', 'email',]
    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return self.email
    
    
 
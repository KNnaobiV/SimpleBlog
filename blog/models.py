from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
# Model manager for the publish method
class PublishedManager(models.Manager):
    def get_querset(self):
        return super(PublishedManager, self).get_queryset()\
            .filter(status='published')

# Model for the blog admin
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'), ('published', 'Published'),
    )
    #image = models.ImageField()
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    #body = models.TextField()
    body = RichTextUploadingField(blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='draft')
    
    objects = models.Manager() # Default object
    published = PublishedManager() # Custom manager
    
    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,self.slug])
    
    tags = TaggableManager()
    
    
class About(models.Model):
    #title = models.CharField(max_length=250, blank=True)
    body = models.TextField()
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.body


class Contact(models.Model):
    #title = models.CharField(max_length=50, blank=True)
    body = models.TextField()
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.body


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, 
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('created',)
        
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
from django.contrib.sitemaps import Sitemap
from .models import Post, Contact, About


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    
    def items(self):
        return Post.published.all()
    
    def lastmod(self, obj):
        return obj.updated
    

class AboutSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9
    
    def items(self):
        return About.body
    
    def lastmod(self, obj):
        return obj.updated
    

class ContactSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    
    def items(self):
        return Contact.body
    
    def lastmod(self, obj):
        return obj.updated
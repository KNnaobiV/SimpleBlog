from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    #post views
    path('', views.post_list, name='home'),
    #path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail,
         name='post_detail'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('about/', views.about_view, name='about_page'),
    path('contact/', views.contact_view, name='contact_page'),
    #path('contact/', ContactView.as_view(), name='contact_page'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
]
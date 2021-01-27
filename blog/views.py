from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, About, Contact
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from taggit.models import Tag
from django.db.models import Count
from .forms import CommentForm

# Create your views here.
#CLASS BASED VIEWS
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 4
    template_name = 'blog/post/list.html'

    
def post_list(request, tag_slug=None):
    """Handles the posts listing on the homepage."""
    posts = Post.published.all()
    object_list = Post.published.all()
    
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    
    paginator = Paginator(object_list, 4) # 4 posts per page
    page = request.GET.get('page')
    #paginator logic
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages) # edit for error message
    return render(request, 'blog/post/list.html', {'posts': posts, 
                                                   'page': page, 'tag': tag})
    

def contact_view(request):
    return render(request, 'blog/contact.html', {'contact': Contact.objects.filter(active=True)})

def about_view(request):
    about = About.objects.filter(active=True)
    return render(request, 'blog/about.html', {'about': about})

def post_detail(request, year, month, day, post):
    """Handles the view of the post once it has been clicked on."""
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year, publish__month=month, 
                             publish__day=day)
    
    #List of active comments for post
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment but don't save to DB yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the DB
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
        .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
        .order_by('-same_tags', '-publish')[:4]
   
    return render(request, 'blog/post/detail.html', {'post': post, 
                  'similar_posts': similar_posts, 'comments': comments, 
                  'new_comment': new_comment, 'comment_form': comment_form})
    
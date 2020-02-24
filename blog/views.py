from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def contact(request):
    return render(request, 'blog/contact.html', {})

def blog(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/blog.html', {'posts': posts, 'title': 'Blog'})

def singleblog(request):
    return render(request, 'blog/single-blog.html')

def about(request):
    return render(request, 'blog/about.html')

def portfolio(request):
    return render(request, 'blog/portfolio.html')

def portfoliodetails(request):
    return render(request, 'blog/portfolio_details.html')

def elements(request):
    return render(request, 'blog/elements.html')

def contact_process(request):
    return render(request, 'blog/contact_process.php')
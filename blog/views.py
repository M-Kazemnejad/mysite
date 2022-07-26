from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
def blog_view(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single_view(request, pid):
    posts = get_object_or_404(Post, id = pid, status = 1)
    context = {'posts':posts}
    return render(request, 'blog/blog-single.html', context)

def test(request, pid, title):
    posts = get_object_or_404(Post, id = pid)
    context = {'posts':posts}
    return render(request, 'test.html', context)
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
def blog_view(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single_view(request, pid):
    prev_post = next_post = 0
    posts = Post.objects.all()
    first_post = Post.objects.first()
    last_post = Post.objects.last()
    for list_index in range(0, len(posts)): 
        if posts[list_index].id == pid:
            if posts[list_index].id != first_post.id and posts[list_index].id != last_post.id:
                prev_post = posts[list_index - 1]
                next_post = posts[list_index + 1]
            else:
                prev_post = next_post = 0

                
    posts_filtered = get_object_or_404(Post, id = pid, status = 1) 
    context = {'post':posts_filtered , 'prev_post' : prev_post, 'next_post' : next_post }
    return render(request, 'blog/blog-single.html', context)



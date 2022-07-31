from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('blog/blog-latest-post.html')
def latest_post(arg=3):
    posts = Post.objects.all().order_by('-published_date')[:arg]
    return {'posts':posts}
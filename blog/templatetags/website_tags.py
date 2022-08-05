from django import template
from blog.models import Post, Category

register = template.Library()

@register.inclusion_tag('website/index-recent-post.html')
def recent_post(arg=6):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts':posts}
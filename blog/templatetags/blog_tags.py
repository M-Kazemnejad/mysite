from django import template
from blog.models import Post, Category

register = template.Library()

@register.inclusion_tag('blog/blog-latest-post.html')
def latest_post(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-category.html')
def post_category():
    categories = Category.objects.all()
    posts = Post.objects.all()
    category_dict = dict()
    for cat in categories:
        count = posts.filter(category_id=cat).count()
        category_dict[cat]=count
    return {'categories':category_dict}
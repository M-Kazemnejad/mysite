from django import template
from blog.models import Post, Category

register = template.Library()


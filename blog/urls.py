from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='blog'),
    path('<int:pid>', blog_single_view, name='blog_single'),
    path('category/<str:cat_name>', blog_view, name='blog_category'),
    path('author/<str:author_username>', blog_view, name='author'),
    path('search/', search_view , name='search'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
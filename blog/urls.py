from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='blog'),
    path('blog-single/', blog_single_view, name='blog_single'),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
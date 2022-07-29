from django.contrib import admin
from blog.models import Post, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title' , 'author' ,'counted_views', 'status', 'published_date', 'created_date', 'updated_date')

admin.site.register(Post,PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(Category, CategoryAdmin)
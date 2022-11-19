from django.contrib import admin
# from .models import Category, Author, Post, Comment, PostCategory
from .models import Category, Author, Post, Comment, PostCategory
# Register your models here.

admin.site.register(Category)
admin.site.register(Author)
# admin.site.register(Post)
admin.site.register(Comment)
# admin.site.register(PostCategory)

class PostCategoryInLine(admin.TabularInline):
    model = PostCategory
    fk_name = 'postThrough'
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [PostCategoryInLine]


admin.site.register(Post, PostAdmin)

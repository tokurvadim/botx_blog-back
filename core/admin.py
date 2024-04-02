from django.contrib import admin

from core.models import User, Page, Page_Category, Category, Comment

@admin.register(User)
class User(admin.ModelAdmin):
    pass

@admin.register(Page)
class Page(admin.ModelAdmin):
    pass

@admin.register(Page_Category)
class Page_Category(admin.ModelAdmin):
    pass

@admin.register(Category)
class Category(admin.ModelAdmin):
    pass

@admin.register(Comment)
class Comment(admin.ModelAdmin):
    pass

from django.contrib import admin
from .models import Book, Category

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','price','stock')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    


from django.contrib import admin
from .models import Student
from .models import movie
# Register your models here.
list_display=("address","marks","name")
search_fields =("name")
list_filter=('created_at')
admin.site.register(Student)

list_display=("name","reviews","rel_date")
search_fields =("name")
list_filter=('created_at')
admin.site.register(movie)
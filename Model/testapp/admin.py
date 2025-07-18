from django.contrib import admin
from .models import Student
# Register your models here.
list_display=("address","marks","name")
search_fields =("name")
list_filter=('created_at')
admin.site.register(Student)
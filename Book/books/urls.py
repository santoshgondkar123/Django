from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
    path('', views.add_to_cart, name='add_to_cart'),
    

]


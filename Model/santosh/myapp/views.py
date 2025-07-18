from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Student
from myapp.models import movie
# Create your views here.
def hello_views(request):
    # reading data from database
    #model.object.all()
    stu_list=Student.objects.all()
    return render(request,'hello.html',{'stu_list':stu_list})

def movie_views(request):
    # reading data from database
    #model.object.all()
    movie_list=movie.objects.all()
    return render(request,'movie.html',{'movie_list':movie_list})

from django.shortcuts import render

# Create your views here.
def company_views(request):
    return render(request,'testapp/company.html')

def list1_views(request):
    Cname= "Tcs"
    Caddress ="Badlapur" 
    CRating= "25.5"
   
    return render(request, 'testapp/list1.html',{'Cname':Cname, 'Caddress':Caddress , 'CRating':CRating})

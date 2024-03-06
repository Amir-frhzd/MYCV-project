from django.shortcuts import render

from django.http import HttpResponse

def index_view(request):
    context={'name':'Amirreza','lastname':'Farahzadi','email':'Amirrezafarahzadi@gmail.com','phone':'09355001378'}
    return render(request,'website/index.html',context)
    

# Create your views here.

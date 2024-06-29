#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("this is new files")
    return render(request,'home.html')

def Login(request):
    return render(request,'Login.html')



def about(request):
    #return HttpResponse("this is about")
    return render(request,'about.html')


    
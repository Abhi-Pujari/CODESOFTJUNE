from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def show(request):
    res='Hello, my name is abhi'

    anchor ="""
     <a href = "con-view">Go to contact</a>
    
    """
    return HttpResponse([res,anchor])

def school(request):
    return HttpResponse('<h2>My school name is RP</h2>')

def contact(request):   
    return HttpResponse('9763330411')
    
  
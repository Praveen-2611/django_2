from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def fun(request):
    return HttpResponse("<h1><marquee>Hello This Is Praveen</h1></marquee>")
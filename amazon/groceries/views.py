from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def vegtables(request):
    return HttpResponse('<h1>vegtables are good for health.....💪💪💪💪💪💪💪</h1>')
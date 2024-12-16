from django.shortcuts import render

# Create your views here.
def ex1(request):
    return render(request,'ex1.html')
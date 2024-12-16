from django.shortcuts import render

# Create your views here.
def conditions(request):
    p={'name':'Praveen','age':22}
    return render(request,'conditions.html',p)




def looping(request):
    p={'name':'Praveenkumar'}
    return render(request,'looping.html',p)
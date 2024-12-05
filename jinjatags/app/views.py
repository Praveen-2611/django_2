from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    p={'name':'Praveen','id':468}
    return render(request,'jinja_print.html',p)
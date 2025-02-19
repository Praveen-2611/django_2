from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse

def insert_student(request):
    sto=StudentForm()
    p={'sto':sto}
    if request.method=='POST':
        to=StudentForm(request.POST)
        if to.is_valid():
            to.save()
            return HttpResponse('created')
        else:
            return HttpResponse('notcreated')

    return render(request,'insert_student.html',p)



# def insert_topic_by_forms(request):
#     eto=TopicModelForm()
#     p={'eto':eto}
#     if request.method=='POST':
#         to=TopicModelForm(request.POST)
#         if to.is_valid():
#             to.save()
#             lto=Topic.objects.all()
#             p={'lto':lto}
#             return render(request,'display_topic_by_forms.html',p)
#             # return HttpResponse('new object is created')
#         else:
#             return HttpResponse('invalid data')

#     return render(request,'insert_topic_by_forms.html',p)
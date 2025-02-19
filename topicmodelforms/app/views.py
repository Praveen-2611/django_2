from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.


def insert_topic_by_forms(request):
    eto=TopicModelForm()
    p={'eto':eto}
    if request.method=='POST':
        to=TopicModelForm(request.POST)
        if to.is_valid():
            to.save()
            lto=Topic.objects.all()
            p={'lto':lto}
            return render(request,'display_topic_by_forms.html',p)
            # return HttpResponse('new object is created')
        else:
            return HttpResponse('invalid data')

    return render(request,'insert_topic_by_forms.html',p)


def insert_webpage_by_form(request):
    ewo=WebpageModelForm()
    p={'ewo':ewo}
    if request.method=='POST':
        wo=WebpageModelForm(request.POST)
        if wo.is_valid():
            wo.save()
            lwo=Webpage.objects.all()
            p={'lwo':lwo}

            return render(request,'display_webpage_by_forms.html',p)
            # return HttpResponse('new object is created')
        else:
            return HttpResponse('invalid data')

    return render(request,'insert_webpage_by_form.html',p)



def insert_acces_by_forms(request):
    eao=AccessModelForm()
    p={'eao':eao}
    if request.method=='POST':
        ao=AccessModelForm(request.POST)
        if ao.is_valid():
            ao.save()
            return HttpResponse('new object is created')
        else:
            return HttpResponse('invalid')


    return render(request,'insert_acces_by_forms.html',p)



def display_topic_by_forms(request):
    lto=Topic.objects.all()
    p={'lto':lto}
    return render(request,'display_topic_by_forms.html',p)



def display_webpage_by_forms(request):
    lwo=Webpage.objects.all()
    p={'lwo':lwo}

    return render(request,'display_webpage_by_forms.html',p)
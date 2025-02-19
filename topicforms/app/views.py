from django.shortcuts import render
from app.models import *
from django.http import HttpResponse


# Create your views here.


def insert_topic(request):
    if request.method=='POST':
        tname=request.POST['tname']
        lto=Topic.objects.get_or_create(tname=tname)
        if lto[1]:
            return HttpResponse(f'new {tname} object is created😎😎😎😎😎')
        else:
            return HttpResponse('the given object is already exists🤣🤣🤣🤣🤣🤣')



    return render(request,'insert_topic.html')

def insert_webpage(request):
    lto=Topic.objects.all()
    p={'lto':lto}
    if request.method=='POST':
        wname=request.POST['wname']
        url=request.POST['url']
        email=request.POST['email']
        tname=request.POST['tname']
        tobj=Topic.objects.get(tname=tname)
        lwo=Webpage.objects.get_or_create(tname=tobj,wname=wname,url=url,email=email)       
        if lwo[1]:
            return HttpResponse(f'new {wname} object is created😎😎😎😎😎')
        else:
            return HttpResponse('the given object is already exists🤣🤣🤣🤣🤣🤣')


    return render(request,'insert_webpage.html',p)

def insert_accessrecord(request):
    lwo=Webpage.objects.all()
    p={'lwo':lwo}
    if request.method=='POST':
        aname=request.POST['aname']
        wname=request.POST['wname']
        wobj=Webpage.objects.get(wname=wname)
        lao=Access_record.objects.get_or_create(wname=wobj,aname=aname)
        if lao[1]:
            return HttpResponse(f'new {aname} object is created😎😎😎😎😎')
        else:
            return HttpResponse('the given object already exists🤣🤣🤣🤣')
    return render(request,'insert_accessrecord.html',p)

def checkbox(request):
    lco=Topic.objects.all()
    p={'lco':lco}
    # if request.method=='POST':
    #     wname=request.POST['wname']
    #     url=request.POST['url']
    #     email=request.POST['email']
    #     tname=request.POST['tname']
    #     tobj=Topic.objects.get(tname=tname)
    #     lwo=Webpage.objects.get_or_create(tname=tobj,wname=wname,url=url,email=email)       
    #     if lwo[1]:
    #         return HttpResponse(f'new {wname} object is created😎😎😎😎😎')
    #     else:
    #         return HttpResponse('the given object is already exists🤣🤣🤣🤣🤣🤣')
    return render(request,'checkbox.html',p)
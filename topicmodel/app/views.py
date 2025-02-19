from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    tn=input('enter the topicname:- ')

    tod=Topic.objects.get_or_create(tname=tn)
    if tod[1]:
        return HttpResponse('new topic is created😎😎😎😎')
    else:
        return HttpResponse('topic is already exist🤣🤣🤣🤣')


def insert_webpage(request):
    tn=input('enter the topicname:- ')
    wn=input('enter the webpagename:- ')
    url=input('enter the url:-')
    email=input('enter the email:- ')

    lto=Topic.objects.filter(tname=tn)
    if lto:
        wo=Webpage.objects.get_or_create(tname=lto[0],wname=wn,url=url,email=email)

        if wo[1]:
            return HttpResponse('new webpage is create😎😎😎😎')
        else:
            return HttpResponse('webpage is already exist🤣🤣🤣🤣')
    else:
        return HttpResponse('the topic which u gave is not exist in the data base😒😒😒😒😒')




def insert_accessrecord(request):
    pk=input('enter webpage id:- ')
    date=input('enter date:- ')


    lwo=Webpage.objects.filter(id=pk)
    if lwo:
        ato=Access_Records.objects.get_or_create(wname=lwo[0],date=date)

        if ato[1]:
            return HttpResponse(' new access_record is create😎😎😎😎')
        else:
            return HttpResponse('accessrecord is already exist🤣🤣🤣🤣')
    else:
        return HttpResponse('the webpage which u gave is not exist in the data base😒😒😒😒😒')
    


#displaying the data in front end


def display_topic(request):
    lto=Topic.objects.all()
    d={'p':lto}
    return render(request,'display_topic.html',d)

def display_webpages(request):
    lwo=Webpage.objects.all()
    d={'lwo':lwo}
    return render(request,'display_webpages.html',d)
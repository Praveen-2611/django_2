from django.db import models

# Create your models here.


class Topic(models.Model):
    tname=models.CharField(primary_key=True,max_length=100)
    

    def __str__(self):
        return self.tname


class Webpage(models.Model):
    tname=models.ForeignKey(Topic,on_delete=models.CASCADE)
    wname=models.CharField(max_length=100,primary_key=True)
    url=models.URLField()
    email=models.EmailField()


    def __str__(self):
        return self.wname
    
class Access_record(models.Model):
    wname=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    aname=models.CharField(max_length=100)


    def __str__(self):
        return self.aname
    








# def insert_emp(request):
#     eno=int(input('enter the empno:- '))
#     ename=input('enter the ename:- ')
#     job=input('enter job:- ')
#     sal=int(input('enter the sal:- '))
#     hiredate=input('enter the date:- ')
#     comm=input('enter the comm:- ')
#     if comm:
#         comm=int(comm)
#     else:
#         comm=None
#     mgr=input('enter the mgr:- ')
#     if mgr:
#         mgr=int(mgr)
#         mgro=Emp.objects.get(empno=mgr)
#     else:
#         mgro=None
#     dno=input('enter the dno:- ')
#     deptobj=Dept.objects.get(dno=dno)
#     eto=Emp.objects.get_or_create(empno=eno,ename=ename,job=job,sal=sal,hiredate=hiredate,comm=comm,mgr=mgro,dno=deptobj)
#     if eto:
#         # return HttpResponse('new emp is created😎😎😎😎😎')
#         # rendering the html page by views
#         leo=Emp.objects.all()
#         d={'p':leo}
        


#         return render(request,'display_emp.html',d)
#     else:
#         return HttpResponse('the given  objects already exist🤣🤣🤣🤣🤣')
  
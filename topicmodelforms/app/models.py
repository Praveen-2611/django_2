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
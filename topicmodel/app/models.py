from django.db import models

# Create your models here.


class Topic(models.Model):
    tname=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.tname


class Webpage(models.Model):
    tname=models.ForeignKey(Topic,on_delete=models.CASCADE)
    wname=models.CharField(max_length=100)
    url=models.URLField(null=True)
    email=models.EmailField(default='ntg@gmail.com')

    def __str__(self):
        return self.wname



class Access_Records(models.Model):
    wname=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return str(self.wname)
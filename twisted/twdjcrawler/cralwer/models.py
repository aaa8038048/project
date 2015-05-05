from django.db import models

# Create your models here.
class Task(models.Model):
    url=models.CharField("url",max_length=100)
    cre=models.CharField("crawler re",max_length=300)
    status=models.IntegerField("status",default=0)
    def __unicode__(self):
        return "%s<-->%d" %(self.url,self.status)
class Proxy(models.Model):
    ip=models.CharField("ip",max_length=15)
    status=models.IntegerField("status",default=0)
    port=models.CharField("port",max_length=10)
    area=models.CharField("area",max_length=30)
    speed=models.FloatField("speed",null=True)
    def __unicode__(self):
        return "%s<-->%f" %(self.url,self.speed)    
class Tclient(models.Model):
    name=models.CharField("name",max_length=20)
    add_time=models.DateTimeField("add_time",auto_now=True)
    def __unicode__(self):
        return "%s<-->%d" %self.name    
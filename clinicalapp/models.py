from django.db import models

# Create your models here.
class patient(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    age = models.IntegerField()
    
class clinicaldata(models.Model):
    COMPONENT_NAMES =[('hw','height/weight'),('bp','bloodpressure'),('heartrate','heart rate')]
    componentname = models.CharField(choices=COMPONENT_NAMES,max_length = 255)
    componentvalue = models.CharField(max_length = 255)
    measureddatetime = models.DateTimeField(auto_now_add= True)
    patient =  models.ForeignKey(patient,on_delete = models.CASCADE)
        


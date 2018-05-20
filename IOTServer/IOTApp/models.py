from django.db import models
from django.utils import timezone
from IOTSite import dictionary as dic

# Create your models here.
#=====================================
# 
#=====================================
class tMeasure(models.Model):    
    MeasureDT = models.CharField(blank=False,null=True,max_length=20,verbose_name="Measured DateTime")
    EquipNo = models.CharField(blank=False,null=True,max_length=20,verbose_name="Controller No")
    ControllerNo = models.CharField(blank=False,null=True,max_length=20,verbose_name="ControllerNo No")
    SensorNo = models.CharField(blank=False,null=True,max_length=20,verbose_name="Sensor No")
    RcvDT = models.CharField(blank=False,null=True,max_length=20,verbose_name="Received DateTime")
    SndDT = models.CharField(blank=False,null=True,max_length=20,verbose_name="Send DateTime")    
    Value = models.CharField(blank=False,null=True,max_length=1000,verbose_name="Values")

    #for translate to local lanuage
    MeasureDT.verbose_name = dic.getName(MeasureDT.verbose_name)
    EquipNo.verbose_name = dic.getName(EquipNo.verbose_name)
    ControllerNo.verbose_name = dic.getName(ControllerNo.verbose_name)
    SensorNo.verbose_name = dic.getName(SensorNo.verbose_name)
    Value.verbose_name = dic.getName(Value.verbose_name)
    RcvDT.verbose_name = dic.getName(RcvDT.verbose_name)

    def __str__(self):
        return "%s %s %s %s %s" %(self.MeasureDT,self.EquipNo,self.ControllerNo,self.SensorNo,self.Value)

    class Meta:
        verbose_name="Measure"
        verbose_name_plural = "Measure"  

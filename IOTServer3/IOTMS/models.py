from django.db import models
from IOTSite import dictionary as dic
from django.db.models import Max

#=====================================
# common funtins
#=====================================
def genSeviceReqNo(self):

    strInOutDate = str(self.InYMD).replace("-","")
    
    if self.ServiceReqSeq == None:
        if self.ServiceReqNo == "" or self.ServiceReqNo == None:
            NewNo = tServiceReq.objects.filter(ServiceReqNo__contains=strInOutDate).aggregate(maxno=Max('ServiceReqNo'))
            if NewNo['maxno'] != None or NewNo['maxno'] == "":
                self.ServiceReqNo = "MS" + strInOutDate + str(int(NewNo['maxno'][-3:]) + 1).rjust(3,'0')
            else:
                self.ServiceReqNo = "MS" + strInOutDate + '001'  

#=====================================
# Master Data
#=====================================
class tDept(models.Model):    
    DeptSeq = models.AutoField(primary_key=True,verbose_name="Department Sequence")
    DeptNo = models.CharField(blank=False,null=True,max_length=20,verbose_name="Department No")
    DeptName = models.CharField(blank=False,null=True,max_length=20,verbose_name="Department Name")

    #for translate to local lanuage
    DeptSeq.verbose_name = dic.getName(DeptSeq.verbose_name)
    DeptNo.verbose_name = dic.getName(DeptNo.verbose_name)
    DeptName.verbose_name = dic.getName(DeptName.verbose_name)

    def __str__(self):
        return "%s" %(self.DeptName)

    class Meta:
        verbose_name="Department"
        verbose_name_plural = "Department"  

    Meta.verbose_name = dic.getName(Meta.verbose_name)
    Meta.verbose_name_plural = dic.getName(Meta.verbose_name_plural)

class tEmp(models.Model):    
    EmpSeq = models.AutoField(primary_key=True,verbose_name="Employee Sequence")
    EmpNo = models.CharField(blank=False,null=True,max_length=20,verbose_name="Employee No")
    EmpName = models.CharField(blank=False,null=True,max_length=20,verbose_name="Emplyee Name")

    #for translate to local lanuage
    EmpSeq.verbose_name = dic.getName(EmpSeq.verbose_name)
    EmpNo.verbose_name = dic.getName(EmpNo.verbose_name)
    EmpName.verbose_name = dic.getName(EmpName.verbose_name)

    def __str__(self):
        return "%s" %(self.EmpName)

    class Meta:
        verbose_name="Employee"
        verbose_name_plural = "Employee"  

    Meta.verbose_name = dic.getName(Meta.verbose_name)
    Meta.verbose_name_plural = dic.getName(Meta.verbose_name_plural)

class tEquipment(models.Model):    
    EquipSeq = models.AutoField(primary_key=True,verbose_name="Equipment Sequence")
    EquipNo = models.CharField(blank=False,null=False,max_length=20,verbose_name="Equipment No")
    EquipName = models.CharField(blank=False,null=True,max_length=20,verbose_name="Equipment Name")
    EquipType = models.CharField(blank=False,null=True,max_length=20,verbose_name="Equipment Type")
    DeptSeq = models.ForeignKey(tDept,blank=True,null=True,on_delete=models.SET_NULL,related_name='+',db_column="DeptSeq",verbose_name="Use Department")
    Remark = models.CharField(blank=True,null=True,max_length=20,verbose_name="Remark")

    #for translate to local lanuage
    EquipSeq.verbose_name = dic.getName(EquipSeq.verbose_name)
    EquipNo.verbose_name = dic.getName(EquipNo.verbose_name)
    EquipName.verbose_name = dic.getName(EquipName.verbose_name)
    EquipType.verbose_name = dic.getName(EquipType.verbose_name)
    DeptSeq.verbose_name = dic.getName(DeptSeq.verbose_name)
    Remark.verbose_name = dic.getName(Remark.verbose_name)    

    def __str__(self):
        return "%s" %(self.EquipName)

    class Meta:
        verbose_name="Equipment"
        verbose_name_plural = "Equipment"  

    Meta.verbose_name = dic.getName(Meta.verbose_name)
    Meta.verbose_name_plural = dic.getName(Meta.verbose_name_plural)

#=====================================
# Maintenance
#===================================== 
class tServiceReq(models.Model):    
    ServiceReqSeq = models.AutoField(primary_key=True,verbose_name="Service Request Sequence")
    ServiceReqNo = models.CharField(blank=True,null=False,max_length=20,verbose_name="Service Request No")
    InYMD = models.DateField(null=False,verbose_name="Receipt Date")
    EquipSeq = models.ForeignKey(tEquipment,blank=True,null=True,on_delete=models.SET_NULL,related_name='+',db_column="EquipSeq",verbose_name="Equipment")
    ReqEmpName = models.CharField(blank=False,null=True,max_length=20,verbose_name="Request Person")
    InEmpSeq = models.ForeignKey(tEmp,blank=True,null=True,on_delete=models.SET_NULL,related_name='+',db_column="InEmpSeq",verbose_name="Receipt Employee")
    FindYM = models.DateField(null=False,verbose_name="Find Date")
    ErrorArea = models.CharField(blank=True,null=True,max_length=20,verbose_name="Failure Location")
    WHLocation = models.CharField(blank=True,null=True,max_length=20,verbose_name="Warehouse Location")

    #for translate to local lanuage
    ServiceReqSeq.verbose_name = dic.getName(ServiceReqSeq.verbose_name)
    ServiceReqNo.verbose_name = dic.getName(ServiceReqNo.verbose_name)
    InYMD.verbose_name = dic.getName(InYMD.verbose_name)
    EquipSeq.verbose_name = dic.getName(EquipSeq.verbose_name)
    ReqEmpName.verbose_name = dic.getName(ReqEmpName.verbose_name)
    InEmpSeq.verbose_name = dic.getName(InEmpSeq.verbose_name)    
    FindYM.verbose_name = dic.getName(FindYM.verbose_name)
    ErrorArea.verbose_name = dic.getName(ErrorArea.verbose_name)
    WHLocation.verbose_name = dic.getName(WHLocation.verbose_name)    

    def __str__(self):
        return "%s %s %s" %(self.ServiceReqNo, self.InYMD, self.ReqEmpName )
        #return self.ServiceReqNo,self.InYMD,self.EquipSeq,self.ReqEmpName,self.FindYM,self.ErrorArea,self.WHLocation

    def save(self, *args, **kwargs):
        genSeviceReqNo(self)
        super(tServiceReq, self).save(*args, **kwargs)  

    class Meta:
        verbose_name="Maintenance Request"
        verbose_name_plural = "Maintenance Request"
        unique_together = (("ServiceReqNo"),)     

    Meta.verbose_name = dic.getName(Meta.verbose_name)
    Meta.verbose_name_plural = dic.getName(Meta.verbose_name_plural)

  
class tServiceRlt(models.Model):    
    ServiceReqSeq = models.ForeignKey(tServiceReq,blank=False,null=True,on_delete=models.SET_NULL,related_name='+',db_column="ServiceReqSeq",verbose_name="Maintenance Request")
    StartYMD = models.DateField(blank=True,null=False,verbose_name="Work start date")
    EndYMD = models.DateField(blank=True,null=True,verbose_name="Work finished date")
    ErrorStatus = models.CharField(blank=True,null=True,max_length=50,verbose_name="Failure Status")
    FinderWork = models.CharField(blank=True,null=True,max_length=50,verbose_name="Finder Action")
    ServiceWork = models.CharField(blank=True,null=True,max_length=50,verbose_name="Repair Work")
    PreventPlan = models.CharField(blank=True,null=True,max_length=50,verbose_name="Faioure Protection plan")
    Remark = models.CharField(blank=True,null=True,max_length=50,verbose_name="References")
    WorkResult = models.CharField(blank=True,null=True,max_length=50,verbose_name="Work Results")
    OutYMD = models.DateField(blank=True,null=True,verbose_name="Issue Date")
    RecEmpName = models.CharField(blank=True,null=True,max_length=20,verbose_name="Recipient")

    #for translate to local lanuage
    ServiceReqSeq.verbose_name = dic.getName(ServiceReqSeq.verbose_name)
    StartYMD.verbose_name = dic.getName(StartYMD.verbose_name)
    EndYMD.verbose_name = dic.getName(EndYMD.verbose_name)
    ErrorStatus.verbose_name = dic.getName(ErrorStatus.verbose_name)
    FinderWork.verbose_name = dic.getName(FinderWork.verbose_name)
    ServiceWork.verbose_name = dic.getName(ServiceWork.verbose_name)    
    PreventPlan.verbose_name = dic.getName(PreventPlan.verbose_name)
    Remark.verbose_name = dic.getName(Remark.verbose_name)
    WorkResult.verbose_name = dic.getName(WorkResult.verbose_name)   
    OutYMD.verbose_name = dic.getName(OutYMD.verbose_name)   
    RecEmpName.verbose_name = dic.getName(RecEmpName.verbose_name)   

    class Meta:
        verbose_name="Maintenance Results"
        verbose_name_plural = "Maintenance Results"

    Meta.verbose_name = dic.getName(Meta.verbose_name)
    Meta.verbose_name_plural = dic.getName(Meta.verbose_name_plural)


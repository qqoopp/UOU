from django.contrib import admin
from IOTMS.models import *
from django.shortcuts import render
#import barcode
#from barcode.writer import ImageWriter

# Register your models here.

# Setting admin title
admin.site.site_header = 'IOT Manage'
admin.site.site_title = 'IOT Manage:'

#============================================================
# Print
def Print_ServiceReq(modeladmin, request, queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)   
    masters = tServiceReq.objects.filter(ServiceReqSeq__in=selected)

    reqno = ""
    for master in masters:        
        reqno = master.ServiceReqNo

    qrurl = request.META['HTTP_HOST'] + request.path + reqno
    return render(request, 'IOTMS/print_MaintenanceReq.html',{'masters':masters, 'qrurl':qrurl})

#============================================================

def Jump_to_Rlt(modeladmin, request, queryset):
    ct = queryset
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)  
    qrurl = 'admin/IOTMS/tServiceRlt/add/'
    return render(request, qrurl)

# Dept
class DeptAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['DeptNo','DeptName']
    list_display_links = list_display
    search_fields = ['DeptNo','DeptName']

admin.site.register(tDept, DeptAdmin)

# Emp
class EmpAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['EmpNo','EmpName']
    list_display_links = list_display
    search_fields = ['EmpNo','EmpName']

admin.site.register(tEmp, EmpAdmin)

# Equipment
class EquipmentAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['EquipNo','EquipName','DeptSeq','EquipType']
    list_display_links = list_display
    search_fields = ['EquipNo','EquipName']

admin.site.register(tEquipment, EquipmentAdmin)

# ServiceReq
class ServiceReqAdmin(admin.ModelAdmin):
    actions = [Print_ServiceReq,Jump_to_Rlt]
    save_on_top = True
    list_display = ['ServiceReqNo','InYMD','EquipSeq','ReqEmpName','FindYM','ErrorArea','WHLocation']
    list_display_links = list_display
    search_fields = ['ServiceReqNo','InYMD']
    fields = ['ServiceReqNo','InYMD','EquipSeq','ReqEmpName','InEmpSeq','FindYM','ErrorArea','WHLocation']
    readonly_fields = ['ServiceReqNo']

admin.site.register(tServiceReq, ServiceReqAdmin)

# ServiceRlt
class ServiceRltAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['ServiceReqSeq','OutYMD','ErrorStatus']
    list_display_links = list_display
    search_fields = ['ServiceReqSeq','OutYMD']

admin.site.register(tServiceRlt, ServiceRltAdmin)







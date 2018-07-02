from django.shortcuts import render
from IOTMS.models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def ServiceReqInfo(request,qreqeustno):    
    masters = tServiceReq.objects.filter(ServiceReqNo=qreqeustno)

    reqno = ""
    for master in masters:        
        reqno = master.ServiceReqNo

    qrurl = request.META['HTTP_HOST'] + request.path + reqno

    return render(request, 'IOTMS/ServiceReqInfo.html',{'masters':masters, 'qrurl':qrurl})
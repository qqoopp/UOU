from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from IOTApp.models import tMeasure
import json

# dashboard
@login_required(login_url='/admin/login/')
@csrf_exempt
def dashboard_mpu(request):

    rowcnt = int(tMeasure.objects.all().count())
    rows = rowcnt - 1000 - 1

    if rows < 0 :
        rows = 0

    rdata = tMeasure.objects.all().filter(SensorNo='MPU').order_by('MeasureDT').values('Value')[rows:]

    sensordata = rdata

    return render(request,'IOTApp/dashboard_mpu.html',{'sensordata':sensordata})


@login_required(login_url='/admin/login/')
@csrf_exempt
def dashboard_dht(request):

    rowcnt = int(tMeasure.objects.all().count())
    rows = rowcnt - 1000 - 1

    if rows < 0 :
        rows = 0

    rdata = tMeasure.objects.all().filter(SensorNo='DHT').order_by('MeasureDT').values('Value')[rows:]

    sensordata = rdata

    return render(request,'IOTApp/dashboard_dht.html',{'sensordata':sensordata})

@login_required(login_url='/admin/login/')
@csrf_exempt
def dashboard_sound(request):

    rowcnt = int(tMeasure.objects.all().count())
    rows = rowcnt - 1000 - 1

    if rows < 0 :
        rows = 0

    rdata = tMeasure.objects.all().filter(SensorNo='SOUND').order_by('MeasureDT').values('Value')[rows:]

    sensordata = rdata

    return render(request,'IOTApp/dashboard_sound.html',{'sensordata':sensordata})



@login_required(login_url='/admin/login/')
@csrf_exempt
def dashboard_guage(request):

    rowcnt = int(tMeasure.objects.all().count())
    rows = 1 #rowcnt - 1000 - 1

    if rows < 0 :
        rows = 0

    rdata = tMeasure.objects.all().filter(SensorNo='DHT').order_by('MeasureDT').values('Value')[rows:]

    sensordata = rdata

    return render(request,'IOTApp/dashboard_guage.html',{'sensordata':sensordata})
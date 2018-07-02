from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from IOTApp.models import tMeasure
import json

@login_required(login_url='/admin/login/')
@csrf_exempt
def chart_guage(request):

    rowcnt = int(tMeasure.objects.all().count())
    rows = 1 #rowcnt - 1000 - 1

    if rows < 0 :
        rows = 0

    rdata = tMeasure.objects.all().filter(SensorNo='dht').order_by('MeasureDT').values('Value')[rows:]

    sensordata = rdata

    return render(request,'IOTApp/chart_guage.html',{'sensordata':sensordata})


@login_required(login_url='/admin/login/')
@csrf_exempt
def chart_org(request):

    rowcnt = int(tMeasure.objects.all().count())
    rows = 1 #rowcnt - 1000 - 1

    if rows < 0 :
        rows = 0

    rdata = tMeasure.objects.all().filter(SensorNo='dht').order_by('MeasureDT').values('Value')[rows:]

    sensordata = rdata

    return render(request,'IOTApp/chart_org.html',{'sensordata':sensordata})


@login_required(login_url='/admin/login/')
@csrf_exempt
def chart_sankey(request):

    rowcnt = int(tMeasure.objects.all().count())
    rows = 1 #rowcnt - 1000 - 1

    if rows < 0 :
        rows = 0

    sensordata = tMeasure.objects.all().filter(SensorNo='dht').order_by('MeasureDT').values('Value')[rows:]
    return render(request,'IOTApp/chart_sankey.html',{'sensordata':sensordata})


@login_required(login_url='/admin/login/')
@csrf_exempt
def chart_line(request,qsensor):

    rowcnt = int(tMeasure.objects.all().count())
    rows = rowcnt - 1000 - 1

    if rows < 0 :
        rows = 0

    sensordata = tMeasure.objects.all().filter(SensorNo=qsensor).order_by('MeasureDT').values('Value')[rows:]
    
    columns = list(json.loads(sensordata[0]['Value']).keys())
    columns.remove('measuredt')
    columns.remove('controller')
    columns.remove('sensor')

    return render(request,'IOTApp/chart_line.html',{'sensordata':sensordata,'columns':columns})


@login_required(login_url='/admin/login/')
@csrf_exempt
def chart_scatter(request,qsensor):

    rowcnt = int(tMeasure.objects.all().count())
    rows = rowcnt - 1000 - 1

    if rows < 0 :
        rows = 0

    sensordata = tMeasure.objects.all().filter(SensorNo=qsensor).order_by('MeasureDT').values('Value')[rows:]
    
    columns = list(json.loads(sensordata[0]['Value']).keys())
    columns.remove('measuredt')
    columns.remove('controller')
    columns.remove('sensor')

    return render(request,'IOTApp/chart_scatter.html',{'sensordata':sensordata,'columns':columns})


@login_required(login_url='/admin/login/')
@csrf_exempt
def chart_table(request,qsensor):

    rowcnt = int(tMeasure.objects.all().count())
    rows = rowcnt - 100 - 1

    if rows < 0 :
        rows = 0

    sensordata = tMeasure.objects.all().filter(SensorNo=qsensor).order_by('MeasureDT').values('Value')[rows:]
    
    columns = list(json.loads(sensordata[0]['Value']).keys())
    columns.remove('measuredt')
    columns.remove('controller')
    columns.remove('sensor')

    return render(request,'IOTApp/chart_table.html',{'sensordata':sensordata,'columns':columns})


@login_required(login_url='/admin/login/')
@csrf_exempt
def chart_map(request,qsensor):

    rowcnt = int(tMeasure.objects.all().count())
    rows = rowcnt - 100 - 1

    if rows < 0 :
        rows = 0

    sensordata = tMeasure.objects.all().filter(SensorNo=qsensor).order_by('MeasureDT').values('Value')[rows:]
    
    columns = list(json.loads(sensordata[0]['Value']).keys())
    columns.remove('measuredt')
    columns.remove('controller')
    columns.remove('sensor')

    return render(request,'IOTApp/chart_map.html',{'sensordata':sensordata,'columns':columns})
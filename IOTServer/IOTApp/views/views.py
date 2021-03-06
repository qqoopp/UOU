from django.shortcuts import render
import json
from django.http import StreamingHttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

from IOTApp.models import *
from django.utils import timezone
from datetime import datetime
import http
from django.http import HttpResponse

import requests
import time

#Data Receiver
#@csrf_protect
@csrf_exempt
def Postjson(request):
    if request.method=="POST":

        try:
            bodydata = request.body.decode("utf-8").replace('\n', '').replace('\r', '').replace(' ', '')
            jdata = json.loads(bodydata)
            
        except Exception as e:
            return StreamingHttpResponse("err: " + str(request.body))

        rdt = timezone.now().strftime("%Y%m%d%H%M%S")

        try:
            postdata = tMeasure(
                MeasureDT=jdata.get('measuredt'),
                EquipNo=jdata.get("data")["controller"],
                ControllerNo=jdata.get("data")["controller"],
                SensorNo=jdata.get("data")["sensor"],
                RcvDT=rdt,
                Value=bodydata,
            )
            postdata.save()

        except Exception as e:
            return StreamingHttpResponse("err: " + str(request.body))

        return StreamingHttpResponse(str(request.body))
        #return HttpResponse(status=200)
    
    return StreamingHttpResponse("GET")

#Data Save to DB
@csrf_exempt
def Transdata(request):
    if request.method=="POST":

        url="http://127.0.0.1:8001/Postjson"

        # read table rows. update senddata
        rdata = tMeasure.objects.all().filter(SndDT__isnull=True)[:1]

        for row in rdata:
            payload = row.Value.strip()
            response = requests.post(url, payload)
            time.sleep(0.1)

            rdt = timezone.now().strftime("%Y%m%d%H%M%S")
            tMeasure.objects.filter(id=row.id).update(SndDT=rdt)
    #    except Exception as e:
    #         return StreamingHttpResponse("err: " + str(request.body))

    #        return StreamingHttpResponse(str(request.body))
        #return HttpResponse(status=200)

    return StreamingHttpResponse("GET")


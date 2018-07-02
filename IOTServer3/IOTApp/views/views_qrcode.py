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
from django.contrib.auth.decorators import login_required

import requests
import time

#Print QR Code
@login_required(login_url='/admin/login/')
@csrf_exempt
def qrcode(request):
    return render(request,'IOTApp/qrcode.html')

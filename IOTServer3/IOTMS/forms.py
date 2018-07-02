from django import forms
from django.contrib.auth.models import User
from .models import *

class tServiceRltForm(forms.ModelForm):
    class Meta:
        model = tServiceRlt
        fields = [
            'ServiceReqSeq','StartYMD','EndYMD','ErrorStatus',
            'FinderWork','ServiceWork','PreventPlan',
            'Remark','WorkResult','OutYMD','RecEmpName',
        ]

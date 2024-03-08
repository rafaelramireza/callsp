from django.shortcuts import render
from django.db import connection
from django.views import View
from django.http import HttpResponse, JsonResponse
from callsp.models import getempdetails
import json

def showdetails(request):
    with connection.cursor() as cursor:
        cursor.callproc('getEmployeeRecords')
        results = cursor.fetchall()
    return render(request, 'index.html', {'getempdetails': results})

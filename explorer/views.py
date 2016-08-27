from django.http import JsonResponse
from django.shortcuts import render
import os
# Create your views here.

def root(req):
    return render(req,'index.html')

def getfiles(req):
    try:
    	path = req.GET['path']
    except:
        path =r'c:\users\bo';
    fs = os.listdir(path)
    return JsonResponse(fs,safe=False)

from django.http import JsonResponse
from django.shortcuts import render
import os
import logging
# Create your views here.

def root(req):
    return render(req,'index.html')

def get(req):
    try:
        path = req.GET['p']
    except:
        path = 'H:'
    names = os.listdir(path)
    objs = [] 
    idx = 0;
    for name in names:
        if name.startswith('.'):
            continue
        _path = os.path.join(path,name)
        _url = 'http://localhost:8000/?p=' + _path
        o = dict(
                id = idx, 
                name=name,
                path=_path,
                url = _url,
                )
        if os.path.isfile(_path):
            size = os.path.getsize(_path)
            if size>5e7:
                o['type']='file'
                o['color']='red'
                objs.append(o)
                idx += 1
        else:
            try:
                os.listdir(o['path'])
                o['type']='folder'
                o['color']='blue'
                objs.append(o)
                idx += 1
            except:
                pass
    return JsonResponse(objs,safe=False) 

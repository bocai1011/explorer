from django.http import JsonResponse
from django.shortcuts import render
import os
import logging
# Create your views here.

def root(req):
    try:
        path = req.GET['p']
    except:
        path = r'H:'
    objs = os.listdir(path)
    ds = []
    fs = []
    for name in objs:
        if name.startswith('.'):
            continue
        _path = os.path.join(path,name)
        o = dict(
                name=name,
                path=_path,
                )
        if os.path.isfile(_path):
            size = os.path.getsize(_path)
            if size>5e7:
                #logging.critical(size)
                fs.append(o)
        else:
            try:
                os.listdir(o['path'])
                ds.append(o)
            except:
                pass
    return render(req,'index.html', {'fs':fs,'ds':ds})

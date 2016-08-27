from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.root),
    url(r'^api/get/$',views.getfiles),
]

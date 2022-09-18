"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework.authtoken import views
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
# from myapp import views
from myapp import views as myapp_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', views.obtain_auth_token),
    path('',include('myapp.urls')),

    path('getthedataofuser/',myapp_view.userdataList),
    path('addyourplace/',myapp_view.placeList),
    path('addyourfield/',myapp_view.fieldList),
    path('getyoufloorname/', myapp_view.fieldnamelist),

    path('addyourdevice/', myapp_view.deviceList),
    path('getallplaces/', myapp_view.placegetList),
    path('getallfields/', myapp_view.fieldgetList),
    path('getallplacesbyonlyplaceidp_id/', myapp_view.placegetallList),
    path('getallfieldsbyonlyplaceidp_id/', myapp_view.fieldgetallList),
    
    path('getpostdeviceStatus/', myapp_view.devicePinStatus),
    path('webhookapi/', myapp_view.webhook),
    # path('getpostPinName/',views.allDeviceSerializers.as_view()),
    path('subuseraccess/', myapp_view.subuaccess),
    path('subuserpalceaccess/', myapp_view.subuplace),
    path('giveaccesstotempuser/', myapp_view.tempU),
    path('getalldatayouaddedtempuser/', myapp_view.tempulist),
    path('getalldevicesbyonlyfieldf_id/', myapp_view.devicegetallList),
    path('getyouplacename/', myapp_view.placenamelist),
    path('getuid/', myapp_view.useridList),
    path('getalldatayouadded/', myapp_view.subuplaceget),
    path('subuserfindall/', myapp_view.subuserfind),
    path('subfindsubdata/', myapp_view.subuserfindsubuser),
    path('notification/', myapp_view.fire),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

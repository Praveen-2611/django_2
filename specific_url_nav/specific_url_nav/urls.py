from django.contrib import admin
from django.urls import path,include
import csk,rcb

urlpatterns = [
    path('admin/', admin.site.urls),
    path('csk/',include('csk.urls')),
    path('rcb/',include('rcb.urls')),
]
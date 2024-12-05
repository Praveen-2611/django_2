from django.urls import path
from groceries.views import *


urlpatterns = [
    path('vegtables/',vegtables,name='vegtables'),
]

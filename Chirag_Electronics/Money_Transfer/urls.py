from django.urls import path,URLPattern
from . import views

urlpatterns=[
    path('transfer',views.Money_Transfer,name="Money_Transfer")
]
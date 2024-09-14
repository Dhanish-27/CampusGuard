from django.urls import path
from . import views

urlpatterns = [
    path("",views.send_email_view,name="send_email_view"),
    path("checkinside",views.checkinside,name="checkinside")
]

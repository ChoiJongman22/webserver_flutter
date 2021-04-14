from django.urls import path,include
from .views import randomWebrtc

urlpatterns=[
    path("<int:id>/",randomWebrtc)
]
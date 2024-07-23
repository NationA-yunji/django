from django.urls import path
from .views import get_admins

urlpatterns = [
    path("admins/", get_admins, name="get_admins"),
]

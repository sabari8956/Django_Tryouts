from .views import index
from django.urls import path

urlpatterns = [
    path('', index, name="api_home"),
]
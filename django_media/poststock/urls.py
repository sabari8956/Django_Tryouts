from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("logout", logout_view, name="logout"),
    path("register", register_view, name="register"),
    path("login", login_view, name="login"),
]
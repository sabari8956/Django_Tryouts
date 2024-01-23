from django.urls import path 
from . import views
from .views import GoogleLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

urlpatterns = [
    path('', views.index , name="index" ),
    path('accounts/social/login/google/', 
         GoogleLoginView,
         name='google_login'),
]

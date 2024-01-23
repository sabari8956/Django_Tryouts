from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request, "user/index.html")


from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

class GoogleLoginView(GoogleOAuth2Adapter):
    ...

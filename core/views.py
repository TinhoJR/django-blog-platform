from django.shortcuts import render
from django.views.generic import View
from . communication import CustomEmail
from . utils import get_location
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# LOGIN EMAIL

class LoginRedirectView(View):


    def get(self,request, *args, **kwargs):
        # ip = request.META.get("HTTP_X_FORWARDED_FOR")
        # id = get_location(ip)
        message = f"""YOU JUST LOGGED IN, IF YOU DIDNT DO THIS PLEASE RESET YOUR PASSWORD
        THE LOG INFO IS BELOW """
        
        receiver = [request.user.email]
        # mail = CustomEmail(CustomEmail.SENDER_SECURITY)
        mail = CustomEmail("security")
        mail.send_email(receiver,"Login Notification",message)
        return HttpResponseRedirect(reverse("dashboard"))


# REGISTRATION EMAIL     



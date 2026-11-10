from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Post
import requests

import  requests
from django.utils.timezone import datetime
import resend

from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"


    # def get(self,request, *args , **kwargs):
        
    #     print(request.META.get("HTTP_X_FORWARDED_FOR"))
    #     print("yoo")
    #     return render(request,self.template_name,{})

    # def test_mail(self):
    #    

    #     r = resend.Emails.send({
    #     "from": "onboarding@resend.dev",
    #     "to": "michealugwu16@gmail.com",
    #     "subject": "Hello World",
    #     "html": "<p>Congrats on sending your <strong>first email</strong>!</p>"
    #     })
    #     print("hello")

    def test_mail(self):
        send_mail(
            subject="test",
            message="testing",
            from_email="onboarding@resend.dev",
            recipient_list=["michealugwu16@gmail.com"],
            fail_silently=False   
        )




    # def get(self, request, *args, **kwargs):

    #     # self.test_mail()

    #     return render(request,self.template_name,{})
    
    def company_list(self):
        headers = {
            'Accept': "application/vnd.api+json"
        }
        endpoint = "https://api.gleif.org/api/v1/lei-records"
        response = requests.get(
            endpoint,
            headers=headers
        )

        feedback = response.json()
        # save_json(feedback)
        company_list = []
        company_data = feedback["data"]
        for data in company_data:
            names = data["attributes"]["entity"]["legalName"]["name"]
            company_list.append(names)
        return company_list

    # def get_context_data(self, **kwargs):
    #     ctx = super(HomeView,self).get_context_data()
    #     ctx["company_name"] = "Lux NG"
    #     ctx["price"] = 9000000000
    #     ctx["rules"] = ["NO STAYING UP LATE","NO FIGHTING","NO FIGHTING","NO ROUGH PLAYS","NO STEALING","NO ROUGH PLAYS","NO ROUGH PLAYS"]
    #     ctx["name"] = "UGWU CHETACHUKWU B"
    #     ctx["discount"] = 15
    #     ctx["tax"] = 20
    #     ctx["other_name"] = "NCHETACHI"
    #     ctx["greeting"] = self.greet()
    #     # ctx["posts"] = Post.objects.all()
    #     #ctx["company_list"] = self.company_list()

    #     return ctx

class AboutView(TemplateView):
    template_name = "about.html"

    

class ListBlogView(ListView):
    model = Post
    template_name = "blog-list.html" 
    context_object_name = "posts"

    def get_queryset(self):
        query = super(ListBlogView,self).get_queryset()
        return query.filter(is_deleted = False)

    
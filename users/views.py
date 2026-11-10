from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from . models import Profile
import pprint
# Create your views here.



class DashBoardView(TemplateView):
    template_name = "dashboard.html"
   
    # def get(self, request, *args, **kwargs):
    #     pprint.pprint(request.META)
    #     return render(request,self.template_name,{})
        
    

# class ProvileView(DetailView):
#     template_name = "profile.html"
#     model = Profile
#     context_object_name = "profile"

class ProvileView(TemplateView):
    template_name = "profile.html"
    


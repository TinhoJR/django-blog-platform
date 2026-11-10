from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,View
from . models import MarketList
from django.urls import reverse_lazy,reverse
from .forms import MarketListForm
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.


class MarketListView(ListView):
    model = MarketList
    context_object_name = "marketlists"
    template_name = "market-list.html"
    

class CreateMarketList(CreateView):
    model = MarketList
    template_name = "create-list.html"
    success_url = reverse_lazy("marketlist")
    form_class = MarketListForm


class UpdateMarketList(UpdateView):
    model = MarketList
    template_name = "create-list.html"
    form_class = MarketListForm
    success_url = reverse_lazy("marketlist") 


class UpdateMarketList(View):

    def post(self,request,*args,**kwargs):

        pk = kwargs.get("pk") 

        try:
            # OBTAIN PK OBJECT
            market_list_item = MarketList.objects.get(pk=pk) 
        except MarketList.DoesNotExist:
            return HttpResponse("THE CONTENT YOU ARE TRYING TO UPDATE DOES NOT EXIST.")
        
        # OBTAIN THE FORM CLASS
        form_class = MarketListForm
        return HttpResponse()



class DeleteMarketList(View):
    # template_name = "delete-market-list.html"
    # success_url = reverse_lazy("marketlist")
    # model = MarketList

   
    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")

        try:
            market_list_item = MarketList.objects.get(pk=pk)
        except MarketList.DoesNotExist:
            return HttpResponse("THE CONTENT YOU ARE RTRYING TO DELETE DOES NOT EXIST.")
        
        market_list_item.delete()
        return HttpResponseRedirect(reverse("marketlist"))
        # return render(
        #     request=request,
        #     template_name="delete-list.html",
        # )

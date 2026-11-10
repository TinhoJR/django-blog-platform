from django.urls import path
from . import views


urlpatterns = [
    path("",views.MarketListView.as_view(),name="marketlist"),
    path("create-list/",views.CreateMarketList.as_view(),name="create-list"),
    path("<int:pk>/update-list/",views.UpdateMarketList.as_view(),name="update-list"),
    path("<int:pk>/delete/",views.DeleteMarketList.as_view(),name="delete-list"),
]
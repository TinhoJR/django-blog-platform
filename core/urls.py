from django.urls import path
from . import views

urlpatterns = [
    path("login/redirect/",views.LoginRedirectView.as_view(),name="login-redirect"),
]
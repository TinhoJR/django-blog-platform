from django.urls import path
from . import auth,profile,views


urlpatterns = [
    path("register/",auth.RegisterView.as_view(),name="register"),
    path("dashboard/",views.DashBoardView.as_view(),name="dashboard"),
    path("dashboard/profile/",views.ProvileView.as_view(),name="profile"),
    path("dashboard/profile/<int:pk>/edit/",profile.EditProfileView.as_view(),name="edit_profile"),
    path("profile/<int:pk>/create/",profile.CreateProfileView.as_view(),name="create_profile"),
]
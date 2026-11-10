from django.views.generic import UpdateView,CreateView
from .models import Profile
from .forms import ProfileViewForm
from django.urls import reverse_lazy


class CreateProfileView(CreateView):
    model = Profile
    template_name = "profile.html"
    form_class = ProfileViewForm
    success_url = reverse_lazy("dashboard")



class EditProfileView(UpdateView):
    model = Profile
    template_name = "edit-profile.html"
    form_class = ProfileViewForm
    success_url = reverse_lazy("profile")


    def get_object(self, queryset = None):
        try:
          # GET PROFILE OBJECT FOR THE LOGGED IN USER
          profile = self.model.objects.get(user=self.request.user)
          
        except self.model.DoesNotExist: 
            # CREATE EMPTY PROFILE FOR THEM, (THEY CAN UPDATE LATER)
            profile = self.model.objects.create(user=self.request.user)

        return profile   



        
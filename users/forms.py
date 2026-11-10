
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


User = get_user_model()


class RegisterForm(forms.ModelForm):

    class Meta :
        model = User
        exclude = ["username"]


class RegisterFormX(UserCreationForm):

    email = forms.EmailField(required=True)
    
    class Meta(UserCreationForm.Meta):
        model = User 
        fields = UserCreationForm.Meta.fields + ('first_name','email')
        




class ProfileViewForm(forms.ModelForm):

    class Meta :
        model = Profile
        exclude = ["user"]


# HOW DOES USERCREATION KNOW ABOUT ABSTRACT USER CLASS TO KNOW ITS ATTRIBUTES


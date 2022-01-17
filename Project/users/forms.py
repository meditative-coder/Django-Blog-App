## This file is created to build custom forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # This class maintains configurations
    class Meta:
        # Specify that this form is going to interact with User model
        model = User
        # Which fields to ask in form
        fields = ['username', 'email', 'password1', 'password2']

# form to update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

# form to update image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

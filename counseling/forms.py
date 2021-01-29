from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import Status


class ProfileSearchForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = {
            'user_joinas',

        }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class meta:
        fields = ['username', 'email', 'password1', 'password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {
            'username',
            'email'
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = {'user'}


class Status_Form(forms.ModelForm):
    class Meta:
        model = Status
        fields = {

            'title',
            'Artical',
            'Artical_img'

        }

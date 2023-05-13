from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('', 'Other'),
)


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    date_of_birth = forms.DateField(required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'date_of_birth', 'gender', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField(required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    profession = forms.CharField(required=False)
    address = forms.CharField(required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['date_of_birth', 'gender', 'profession', 'address', 'image']

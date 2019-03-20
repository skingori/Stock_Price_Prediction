from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True, help_text='Optional.',
                               widget=forms.TextInput(attrs={'class': "form-control"}))
    # first_name = forms.CharField(required=False, help_text='Optional.',
    #                              widget=forms.TextInput(attrs={'class': "form-control"}))
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.',
    #                             widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',
                             widget=forms.EmailInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(required=False, help_text='Optional.',label="Password",
                                widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(required=False, help_text='Optional.',label="Confirm Password",
                                widget=forms.PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

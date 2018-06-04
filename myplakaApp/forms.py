from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import Search


class Form(forms.ModelForm):
    class Meta:
        model=Search
        fields=[
            'owner',
            'date',
            'plaka',
            'phone',
        ]
class SaveForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = [
            'plaka',
            'owner',
            'phone',
            'date',

        ]
"""class BildirimForm(forms.ModelForm):
    class Meta:
        model=Bildirim
        fields = [
            'name',
            'content',
        ]
"""
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Kullanici adini veya sifreyi yanlis girdiniz!")
        return super(LoginForm, self).clean()

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label='Kullanici Adi')
    password1 = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label='Parola Dogrulama', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Sifreler eslesmiyor!")
        return password2
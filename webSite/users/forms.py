from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label = 'Введите логин',
        required=True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )

    #some = forms.ModelChoiceField(queryset = User.objects.all()) #Поле выбора
    password1 = forms.CharField(
        label = 'Введите пароль',
        required=True,
        widget = forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
        label = 'Подтвердите пароль',
        required=True,
        widget = forms.PasswordInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        label = 'Введите email',
        required=True, help_text='*обязательное поле',
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    ) # required=False - необязательное поле


    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class UserUpdateForm(forms.ModelForm):
            username = forms.CharField(
                label = 'Введите логин',
                required=True,
                widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
            )

            email = forms.EmailField(
                label = 'Введите email',
                required=False, help_text='*Необязательное поле',
                widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
            ) # required=False - необязательное поле

            class Meta:
                model = User
                fields = ['username', 'email']

class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Загрузить фото',
        required = False,
        widget = forms.FileInput
    )

    class Meta:
        model = Profile
        fields = ['img']

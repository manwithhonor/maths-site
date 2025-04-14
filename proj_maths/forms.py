from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from proj_maths.models import CustomUser
from django import forms

class SignUpForm(UserCreationForm):
    phone = forms.CharField(max_length=15, help_text='Обязательное поле. Введите действующий номер телефона.')
    age =  forms.IntegerField(help_text='Обязательное поле. Введите ваш возраст.')

    class Meta:
        model = CustomUser
        # model = User
        fields = ('username', 'phone', 'age', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
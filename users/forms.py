from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from .validators import (
    validate_password_length,
    validate_password_uppercase,
    validate_password_lowercase,
    validate_password_digit,
    validate_password_username,
)
# from .widgets import CustomDateInput

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label='Имя')
    last_name = forms.CharField(max_length=30, required=False, label='Фамилия')
    # date_of_birth = forms.DateField(null=True, blank=False, widget=CustomDateInput()) 
     # Изменено на blank=False
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_picture', 'first_name', 'last_name')
        labels = {
            'username': 'Имя пользователя',
            'email': 'Электронная почта',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'profile_picture': 'Фото профиля',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
            'date_of_birth': 'Дата рождения',
        }
        error_messages = {
            'username': {
                'unique': 'Пользователь с таким именем уже существует.'
            },
            'email': {
                'unique': 'Пользователь с такой почтой уже существует.'
            },
            'date_of_birth': {
                'invalid': 'Дата рождения должна быть в формате DD.MM.ГГГГ.'
            },
            'password_mismatch': "Пароли не совпадают.",
            'password1_invalid': "Пароль должен содержать хотя бы 8 символов, включая буквы, цифры и специальные символы.",
        }
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        username = self.cleaned_data.get('username')

        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Пароли не совпадают.')
        
        validate_password_length(password1)
        validate_password_uppercase(password1)
        validate_password_lowercase(password1)
        validate_password_digit(password1)
        validate_password_username(password1, username)
        
        return password2

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
    
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Email или Логин'
        self.fields['password'].label = 'Пароль'
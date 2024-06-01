from django.core.exceptions import ValidationError
import re

def validate_password_length(password):
    if len(password) < 8:
        raise ValidationError('Пароль должен содержать хотя бы 8 символов.')

def validate_password_uppercase(password):
    if not any(char.isupper() for char in password):
        raise ValidationError('Пароль должен содержать хотя бы одну букву в верхнем регистре.')

def validate_password_lowercase(password):
    if not any(char.islower() for char in password):
        raise ValidationError('Пароль должен содержать хотя бы одну букву в нижнем регистре.')

def validate_password_digit(password):
    if not any(char.isdigit() for char in password):
        raise ValidationError('Пароль должен содержать хотя бы одну цифру.')

def validate_password_username(password, username):
    if username and password and username == password:
        raise ValidationError('Пароль не должен совпадать с именем пользователя.')

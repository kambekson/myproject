from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CustomUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Попробуйте сначала найти пользователя по email
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            # Если не удалось, попробуйте найти по юзернейму
            try:
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                return None
        # Проверьте пароль
        if user.check_password(password):
            return user
        return None

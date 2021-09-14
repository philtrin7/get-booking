from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User


class PasswordlessAuthBackend(BaseBackend):

    def authenticate(self, request, username=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            return user
        except User.MultipleObjectsReturned:
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

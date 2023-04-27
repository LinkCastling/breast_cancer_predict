from django.test import TestCase

from app01.models import UserInfo

user_object = UserInfo.objects.filter(username="admin").first()
print(type(user_object.password))



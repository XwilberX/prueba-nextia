import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'nextia1.settings'
django.setup()

from django.contrib.auth.hashers import make_password
from app.models import UserModel

fullname = input("Enter your full name: ")
username = input("Enter your username: ")
email = input("Enter your email: ")
password = input("Enter your password: ")

if UserModel.objects.create(fullname=fullname, username=username, email=email, password=make_password(password)):
    print("User created successfully")
else:
    print("Error creating user")
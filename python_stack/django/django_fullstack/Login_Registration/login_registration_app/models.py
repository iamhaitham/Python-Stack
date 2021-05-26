from django.db import models
from django.shortcuts import HttpResponse
import re
import datetime


class UserManager(models.Manager):
    def validator(self,postData):
        today = datetime.datetime.now().strftime("%Y%m%d")
        errors={}
        if len(postData["first_name"])<2:
            errors["first_name"]="First Name field should be at least 2 characters long!"
        if len(postData["last_name"])<2:
           errors["last_name"]="Last Name field should be at least 2 characters long!" 
        if postData["password"] != postData["confirm_pw"]:
            errors["password"]="Passwords don't match!"
        if postData["password"] == postData["confirm_pw"]:
            if len(postData["password"])<8:
                errors["password"]="Password should be at least 8 characters!"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if postData["date"].replace("-","") > today:
            errors["date"]="Only past dates are accepted!"
        if len(User.objects.filter(email=postData["email"]))>0:
            errors["email"]="This email is already used!"
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    birthday=models.DateField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

def check_email(email):
    if len(User.objects.filter(email=email))==0:
        return False
    else:
        return True

def register(first_name,last_name,email,hashed_pw,birthday):
    return User.objects.create(first_name=first_name,last_name=last_name,email=email,password=hashed_pw,birthday=birthday)

def login_username(username):
    user=User.objects.filter(email=username)
    if len(user)>0:
        return user[0]
    else:
        return None

def get_first_name(username):
    return User.objects.get(email=username).first_name

def get_last_name(username):
    return User.objects.get(email=username).last_name

def get_user_id(username):
    return User.objects.get(email=username).id


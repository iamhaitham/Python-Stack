from django.db import models
import re


class UserManager(models.Manager):
    def validator(self,postData):
        errors={}
        if len(postData["first_name"])<2:
            errors["first_name"]="First Name field should be at least 2 characters long!"
        if len(postData["last_name"])<2:
           errors["last_name"]="Last Name field should be at least 2 characters long!" 
        if postData["password"] != postData["confirm_password"]:
            errors["password"]="Passwords don't match!"
        if postData["password"] == postData["confirm_password"]:
            if len(postData["password"])<8:
                errors["password"]="Password should be at least 8 characters!"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['no_email'] = "Invalid email address!"
        if len(User.objects.filter(email=postData["email"]))>0:
            errors["idential_email"]="This email is already used!"
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

def check_email(email):
    if len(User.objects.filter(email=email))==0:
        return False
    else:
        return True

def register(first_name,last_name,email,hashed_pw):
    return User.objects.create(first_name=first_name,last_name=last_name,email=email,password=hashed_pw)

def login_username(username):
    user=User.objects.filter(email=username)
    if len(user)>0:
        return user[0]
    else:
        return None

def login_username_check(username):
    if len(User.objects.filter(email=username))==0:
        return True
    else:
        return False

def get_first_name(username):
    return User.objects.get(email=username).first_name

def get_last_name(username):
    return User.objects.get(email=username).last_name

def get_user_id(username):
    return User.objects.get(email=username).id


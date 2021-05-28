from django.db import models
import re

class Manage(models.Manager):
    def validator(self,postData):
        errors={}
        if len(postData["first_name"])<2:
            errors["first_name"]="First name must be at least 2 characters"
        if len(postData["last_name"])<2:
            errors["last_name"]="Last name must be at least 2 characters"
        if postData["confirm_pw"]!=postData["password"]:
            errors["confirm_pw"]="Passwords don't match!"
        if len(postData["password"])<8:
            errors["password"]="Password must be at least 8 characters!"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):   
            errors['email'] = "Invalid email address!"
        if len(User.objects.filter(email=postData["email"]))>0:
            errors["email"]="This email is already used!"
        return errors     
    
class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=Manage()

class Message(models.Model):
    message=models.TextField()
    user=models.ForeignKey(User,related_name="messages",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment=models.TextField()
    user=models.ForeignKey(User,related_name="comments",on_delete=models.CASCADE)
    message=models.ForeignKey(Message,related_name="comments",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


def display_all_messages():
    return Message.objects.all()


def create_a_message(message,user_id):
    user=User.objects.get(id=user_id)
    return Message.objects.create(message=message,user=user)


def check_email(email):
    if len(User.objects.filter(email=email))==0:
        return False
    else:
        return True


def create_user(first_name,last_name,email,pw_hash):
    return User.objects.create(first_name=first_name,last_name=last_name,email=email,password=pw_hash)


def check_login(username):
    user=User.objects.filter(email=username)
    if len(user)>0:
        return user[0]
    else:
        return None


def create_a_comment(commentarea,user_id,msg_id):
    user=User.objects.get(id=user_id)
    message=Message.objects.get(id=msg_id)
    return Comment.objects.create(comment=commentarea,user=user,message=message)


def delete_a_post(message_id):
    message=Message.objects.get(id=message_id)
    return message.delete()



from django.db import models

# Create your models here.
class users(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    age=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

def show_db():
    return users.objects.all()

def add_to_db(first_name,last_name,email,age):
    return users.objects.create(first_name=first_name,last_name=last_name,email=email,age=age)

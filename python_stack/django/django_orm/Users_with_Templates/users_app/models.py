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

def add_to_db(fn,ln,em,ag):
    return users.objects.create(first_name=fn,last_name=ln,email=em,age=ag)
    
from django.db import models

# Create your models here.

class Dojo(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=2)
    desc=models.TextField(default="old dojo")
    #ninjas=A list of ninjas in a certain dojo. This is called "Reverse Lookup with related_name".

class Ninja(models.Model):
    dojo=models.ForeignKey(Dojo,related_name="ninjas",on_delete=models.CASCADE)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)

def show_dojos():
    return Dojo.objects.all()

def add_dojo(dojo_name,dojo_city,dojo_state):
    Dojo.objects.create(name=dojo_name,city=dojo_city,state=dojo_state,desc="old dojo")

def add_ninja(ninja_select_dojo,ninja_first_name,ninja_last_name):
    Ninja.objects.create(dojo=Dojo.objects.get(name=ninja_select_dojo),first_name=ninja_first_name,last_name=ninja_last_name)

def Delete(ID):
    Dojo.objects.get(id=ID).delete()
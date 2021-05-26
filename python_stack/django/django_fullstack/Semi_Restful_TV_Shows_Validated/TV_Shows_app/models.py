from django.db import models

class ShowManager(models.Manager):
    def validator(self,postData):
        errors={}
        if len(postData["show_title"])<2:
            errors["show_title"]="Title should be at least 2 characters"
        if len(postData["show_network"])<3:
            errors["show_network"]="Network should be at least 3 characters"
        if len(postData["show_description"])>0:
            if len(postData["show_description"])<10:
                errors["show_description"]="Description should be at least 10 characters"
        return errors

class Show(models.Model):
    title=models.TextField(unique=True)
    network=models.CharField(max_length=45)
    release_date=models.DateField()
    description=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=ShowManager()

def all_shows():
    return Show.objects.all()

def add_shows(show_title,show_network,show_release_date,show_description):
    return Show.objects.create(title=show_title,network=show_network,release_date=show_release_date,description=show_description)

def some_show(show_id):
    return Show.objects.get(id=show_id)

def get_show_id(show_title):
    return Show.objects.get(title=show_title).id

def update(show_id,show_title,show_network,show_release_date,show_description):
    show=Show.objects.get(id=show_id)
    show.title=show_title
    show.network=show_network
    show.release_date=show_release_date
    show.description=show_description
    show.save()

def delete(show_id):
    show=Show.objects.get(id=show_id)
    show.delete()


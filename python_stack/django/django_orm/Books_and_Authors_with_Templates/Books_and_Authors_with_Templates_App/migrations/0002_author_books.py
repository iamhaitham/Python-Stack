# Generated by Django 2.2.4 on 2021-05-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books_and_Authors_with_Templates_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='Books_and_Authors_with_Templates_App.Book'),
        ),
    ]

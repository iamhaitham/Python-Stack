# Generated by Django 2.2.4 on 2021-05-22 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='authors',
            new_name='Author',
        ),
    ]

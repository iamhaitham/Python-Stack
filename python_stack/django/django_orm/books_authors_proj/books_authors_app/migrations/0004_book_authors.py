# Generated by Django 2.2.4 on 2021-05-22 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0003_auto_20210522_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', to='books_authors_app.Author'),
        ),
    ]

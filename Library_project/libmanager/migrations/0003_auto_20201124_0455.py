# Generated by Django 3.1.3 on 2020-11-24 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libmanager', '0002_requested_books_roll_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='books_collection',
            name='availibility',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='books_collection',
            name='borrowed_by',
            field=models.IntegerField(default=0),
        ),
    ]
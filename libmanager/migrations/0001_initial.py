# Generated by Django 3.1.1 on 2020-11-01 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books_collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField()),
                ('book_name', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=120)),
                ('category', models.CharField(max_length=120)),
                ('language', models.CharField(max_length=120)),
            ],
        ),
    ]
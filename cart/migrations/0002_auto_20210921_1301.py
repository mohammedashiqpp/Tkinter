# Generated by Django 3.2.7 on 2021-09-21 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartlist',
            name='user',
        ),
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
    ]

# Generated by Django 3.0.8 on 2020-09-07 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myblog',
            name='image',
        ),
    ]

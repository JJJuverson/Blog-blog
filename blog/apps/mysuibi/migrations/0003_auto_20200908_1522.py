# Generated by Django 3.0.8 on 2020-09-08 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysuibi', '0002_auto_20200907_1059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mysuibi',
            options={'ordering': ['add_time'], 'verbose_name': '我的随笔', 'verbose_name_plural': '我的随笔'},
        ),
    ]

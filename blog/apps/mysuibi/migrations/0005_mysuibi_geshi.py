# Generated by Django 3.0.8 on 2020-09-22 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysuibi', '0004_mysuibi_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysuibi',
            name='geshi',
            field=models.CharField(choices=[('0', 'no'), ('1', 'one')], default='0', max_length=6, verbose_name='格式显示'),
        ),
    ]

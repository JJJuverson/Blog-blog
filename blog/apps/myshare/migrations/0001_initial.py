# Generated by Django 3.0.8 on 2020-09-30 16:35

import datetime
from django.db import migrations, models
import mdeditor.fields
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', help_text='分享标题', max_length=50, verbose_name='分享标题')),
                ('image', stdimage.models.StdImageField(blank=True, null=True, upload_to='path/to', verbose_name='传图片')),
                ('mode', models.CharField(choices=[('0', 'no'), ('1', 'one')], default='0', max_length=6, verbose_name='格式显示')),
                ('type', models.CharField(blank=True, default='', help_text='分享类型', max_length=30, null=True, verbose_name='分享类型')),
                ('content', mdeditor.fields.MDTextField()),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '我的分享',
                'verbose_name_plural': '我的分享',
                'ordering': ['add_time'],
            },
        ),
    ]

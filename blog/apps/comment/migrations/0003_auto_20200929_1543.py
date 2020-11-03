# Generated by Django 3.0.8 on 2020-09-29 15:43

import datetime
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_auto_20200923_1938'),
        ('mysuibi', '0006_auto_20200923_1938'),
        ('comment', '0002_auto_20200908_1301'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommentList',
            new_name='CommentList_blog',
        ),
        migrations.CreateModel(
            name='CommentList_suibi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='用户', max_length=30, verbose_name='用户')),
                ('email', models.CharField(blank=True, default='', help_text='用户邮箱', max_length=30, null=True, verbose_name='用户邮箱')),
                ('content', mdeditor.fields.MDTextField()),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('comment_obj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mysuibi.MySuibi', verbose_name='评论对象')),
            ],
            options={
                'verbose_name': '评论列表',
                'verbose_name_plural': '评论列表',
                'ordering': ['add_time'],
            },
        ),
    ]

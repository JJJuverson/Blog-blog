from datetime import datetime
from django.db import models
from mdeditor.fields import MDTextField
from myblog.models import MyBlog
from mysuibi.models import MySuibi
#from stdimage.models import StdImageField


class CommentList_blog(models.Model):
    comment_obj = models.ForeignKey(MyBlog,verbose_name="评论对象",null=True, on_delete=models.CASCADE)
    name =models.CharField(default="", max_length=30, verbose_name="用户", help_text="用户")
    email = models.CharField(default="", max_length=30, verbose_name="用户邮箱", help_text="用户邮箱",null=True,blank=True)
    content = MDTextField()
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "博客评论列表"
        verbose_name_plural = verbose_name
        ordering = ['add_time']

    def __str__(self):
        return self.content
        
class CommentList_suibi(models.Model):
    comment_obj = models.ForeignKey(MySuibi,verbose_name="评论对象",null=True, on_delete=models.CASCADE)
    name =models.CharField(default="", max_length=30, verbose_name="用户", help_text="用户")
    email = models.CharField(default="", max_length=30, verbose_name="用户邮箱", help_text="用户邮箱",null=True,blank=True)
    content = MDTextField()
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "随笔评论列表"
        verbose_name_plural = verbose_name
        ordering = ['add_time']

    def __str__(self):
        return self.content

from datetime import datetime
from django.db import models
from mdeditor.fields import MDTextField 
from stdimage.models import StdImageField


class MySuibi(models.Model):
    GESHI_CHOICES = (
      ("0", u"no"),
      ("1", u"one")
    )
    title =models.CharField(default="", max_length=50, verbose_name="随笔标题", help_text="随笔标题")
    

    image = StdImageField(max_length=100,
                          upload_to='path/to',
                          verbose_name=u"传图片",
                          variations={'thumbnail': {'width': 100, 'height': 75}},
                          null=True,blank=True)
    mode = models.CharField(max_length=6, choices=GESHI_CHOICES, default="0", verbose_name="格式显示")
    type = models.CharField(default="", max_length=30, verbose_name="随笔类型", help_text="随笔类型",null=True,blank=True)
    
    content = MDTextField()
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "我的随笔"
        verbose_name_plural = verbose_name
        ordering = ['add_time']
    def __str__(self):
        return self.title

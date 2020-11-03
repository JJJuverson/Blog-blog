import xadmin
from .models import MyBlog

class MyBlogAdmin(object):
    list_display = ["id","title", "content", "type","add_time"]
    list_filter = ["title", "content", "type","add_time"]
    search_fields = ["title", "content", "type","add_time"]


xadmin.site.register(MyBlog,MyBlogAdmin)
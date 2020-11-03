import xadmin
from .models import MyShare

class MyShareAdmin(object):
    list_display = ["title", "content", "type","add_time"]
    list_filter = ["title", "content", "type","add_time"]
    search_fields = ["title", "content", "type","add_time"]


xadmin.site.register(MyShare,MyShareAdmin)
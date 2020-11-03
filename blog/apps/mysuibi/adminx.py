import xadmin
from .models import MySuibi

class MySuibiAdmin(object):
    list_display = ["title", "content", "type","add_time"]
    list_filter = ["title", "content", "type","add_time"]
    search_fields = ["title", "content", "type","add_time"]


xadmin.site.register(MySuibi,MySuibiAdmin)
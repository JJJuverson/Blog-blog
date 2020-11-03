import xadmin
from .models import CommentList_blog,CommentList_suibi

class CommentList1Admin(object):
    list_display = ["name", "email", "comment_obj","content","add_time"]
    list_filter = ["name",  "comment_obj","add_time"]
    search_fields = ["name",  "comment_obj","add_time"]


xadmin.site.register(CommentList_blog,CommentList1Admin)


class CommentList2Admin(object):
    list_display = ["name", "email", "comment_obj","content","add_time"]
    list_filter = ["name",  "comment_obj","add_time"]
    search_fields = ["name",  "comment_obj","add_time"]


xadmin.site.register(CommentList_suibi,CommentList2Admin)
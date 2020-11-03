from rest_framework import serializers
from .models import CommentList_blog,CommentList_suibi
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from datetime import datetime

#分页设置类继承
class pagenationset(PageNumberPagination):
    page_size = 5
    page_query_param = 'pageIndex'
    page_size_query_param = 'pageSize'
    max_page_size = 10

class CommentList1_serializer(serializers.ModelSerializer):
    class Meta:
        model = CommentList_blog
        fields = '__all__'

class CommentList2_serializer(serializers.ModelSerializer):
    class Meta:
        model = CommentList_suibi
        fields = '__all__'


@api_view(['POST'])
def CommentListViewSet(request):
    pass
    """
    name = request.POST['name']
    email = request.POST['email']
    content = request.POST['content']
    id = request.POST['id']
    obj = {
        name = name,
        email = email,
        content = content,
        add_time = datetime.datetime.now()
        comment_obj = id
    }
    obj.save()
    """
   
        

    

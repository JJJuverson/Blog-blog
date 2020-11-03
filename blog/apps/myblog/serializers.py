from rest_framework import serializers
from .models import MyBlog
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination


#分页设置类继承
class pagenationset(PageNumberPagination):
    page_size = 5
    page_query_param = 'pageIndex'
    page_size_query_param = 'pageSize'
    max_page_size = 5

class MyBlogserializer(serializers.ModelSerializer):
    class Meta:
        model = MyBlog
        fields = '__all__'



@api_view(['GET'])
def BlogViewSet(request):
    pageIndex = request.GET.get('pageIndex','')
    blog = MyBlog.objects.all()
    count = MyBlog.objects.count()
    pag = pagenationset()
    blog = pag.paginate_queryset(blog,request)
    blogs = MyBlogserializer(blog, many=True)
    return Response({'total':count,'data':blogs.data})
        

    

from rest_framework import serializers
from .models import MyShare
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination


#分页设置类继承 
class pagenationset(PageNumberPagination):
    page_size = 5
    page_query_param = 'pageIndex'
    page_size_query_param = 'pageSize'
    max_page_size = 10

class MyShare_serializer(serializers.ModelSerializer):
    class Meta:
        model = MyShare
        fields = '__all__'



@api_view(['GET'])
def ShareViewSet(request):
    #search_wd = request.GET.get('keywords','')
    pageIndex = request.GET.get('pageIndex','')
    #if search_wd != '':
    #    suibi = MySuibi.objects.filter(title__icontains = search_wd)
    #else:
    share = MyShare.objects.all()
    count = MyShare.objects.count()
    #分页
    pag = pagenationset()
    share = pag.paginate_queryset(share,request)
    shares = MyShare_serializer(share, many=True)
    return Response({'total':count,'data':shares.data})
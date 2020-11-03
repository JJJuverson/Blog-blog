from rest_framework import serializers
from .models import MySuibi
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination


#分页设置类继承
class pagenationset(PageNumberPagination):
    page_size = 5
    page_query_param = 'pageIndex'
    page_size_query_param = 'pageSize'
    max_page_size = 10

class MySuibi_serializer(serializers.ModelSerializer):
    class Meta:
        model = MySuibi
        fields = '__all__'



@api_view(['GET'])
def SuibiViewSet(request):
    pageIndex = request.GET.get('pageIndex','')
    suibi = MySuibi.objects.all()
    count = MySuibi.objects.count()
    pag = pagenationset()
    suibi = pag.paginate_queryset(suibi,request)
    suibis = MySuibi_serializer(suibi, many=True)
    return Response({'total':count,'data':suibis.data})
        

    

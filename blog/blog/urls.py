"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.urls import path

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from myblog.serializers import BlogViewSet
from mysuibi.serializers import SuibiViewSet
from comment.serializers import CommentListViewSet
from myshare.serializers import ShareViewSet




urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    url(r'mdeditor/', include('mdeditor.urls')),
    #path('blog/',include('myblog.urls'))
    path('blog',BlogViewSet),
    path('suibi',SuibiViewSet),
    path('comment',CommentListViewSet),
    path('share',ShareViewSet)
  
    
]




if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path,include
from django.views.static import serve
from bwshop.settings import MEDIA_ROOT
import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from goods.views import GoodsListViewSet,CategoryViewSet
from user_operation.views import UserFavViewset,LeavingMessageViewset
from trade.views import ShoppingCartViewset,OrderViewset

from users.views import *

from rest_framework import routers



router = routers.DefaultRouter()
router.register('goods',GoodsListViewSet)
router.register('category',CategoryViewSet,basename='category')
router.register('code',SmsCodeViewSet,basename='code')
router.register('users',UserViewset,basename='users')
router.register('userfavs',UserFavViewset,basename='userfavs')
router.register('messages',LeavingMessageViewset,basename='messages')
router.register('shopcarts',ShoppingCartViewset,basename='shopcarts')
router.register('orders',OrderViewset,basename='orders')

schema_view = get_schema_view(title='corejson')
urlpatterns = [
    path('xadmin/',xadmin.site.urls),
    # 副文本编辑器的路径
    path('ueditor/',include('DjangoUeditor.urls')),
    # 文件上传的路径
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    path(r'',include(router.urls)),
    path('api-token-auth',views.obtain_auth_token),
    path('login/',obtain_jwt_token),
    path('api-auth/', include('rest_framework.urls')),

    path('docs/',include_docs_urls(title='DRF文档')),
    path('schema/',schema_view)
]
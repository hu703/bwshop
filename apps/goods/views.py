from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

from .serializers import *
from .models import *

from rest_framework.pagination import PageNumberPagination
# from .filters import GoodsFilter
# from django_filters.rest_framework import DjangoFilterBackend


class GoodsPaginetion(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100

# class GoodsListView(APIView):
#     def get(self,request,format=None):
#         goods = Goods.objects.all()
#         goods_seriailzer = GoodsSerializer(goods,many=True)
#         return Response(goods_seriailzer.data)

# class GoodsListView(generics.ListAPIView):
#     pagination_class = GoodsPaginetion
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer


class GoodsListViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    pagination_class = GoodsPaginetion
    queryset = Goods.objects.all().order_by('id')
    serializer_class = GoodsSerializer

    # # 设置筛选
    # filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    # filter_class = GoodsFilter

    # # 设置搜索
    # search_fields = ('=name','goods_brief')
    #
    # # 排序
    # ordering_fields = ('sold_num','add_time')


class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer

class HotSearchsViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取热搜词列表
    """
    queryset = HotSearchWords.objects.all().order_by("-index")
    serializer_class = HotWordsSerializer


class BannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取轮播图列表
    """
    queryset = Banner.objects.all().order_by("index")
    serializer_class = BannerSerializer


class IndexCategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    首页商品分类数据
    """
    queryset = GoodsCategory.objects.filter(is_tab=True, name__in=["生鲜食品", "酒水饮料"])
    serializer_class = IndexCategorySerializer

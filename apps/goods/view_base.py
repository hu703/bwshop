from django.views.generic.base import View
from goods.models import Goods

from django.core import serializers

class GoodsListView(View):
    def get(self,request):
        """
                通过django的view实现商品列表页
                """
        json_list = []
        # 获取所有商品
        goods = Goods.objects.all()[:10]
        '''
            model_to_dict  会出现报错
        '''
        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        # from django.http import HttpResponse
        # # 只能转换dict和list类型
        # import json
        # # 返回json  指明类型
        # return HttpResponse(json.dumps(json_list), content_type='application/json')

        '''
            django serializer  不建议使用
        '''
        # from django.core import serializers
        # from django.http import JsonResponse
        # import json
        # json_data = serializers.serialize('json',goods)
        # json_data = json.loads(json_data)
        # return JsonResponse(json_data,safe=False)

        '''
            常规做法
        '''
        for good in goods:
            json_dict = {}
            json_dict["name"] = good.name
            json_dict["category"] = good.category.name
            json_dict["market_price"] = good.market_price
            json_list.append(json_dict)

        from django.http import HttpResponse
        import json
        return HttpResponse(json.dumps(json_list),content_type='application/json')

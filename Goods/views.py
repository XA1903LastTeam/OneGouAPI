from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from .api import SiwapModelSerializers, SiwapModel
from .api import GoodsModelSerializers, GoodsInfoModel, GoodsModel, GoodsInfoModelSerializers


# Create your views here.
class GetHomeDataView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        # 该请求是根据地区来获取商品数据的，目前数据只有西安地区的数据，所以不需要考虑
        siwap = SiwapModel.objects.all()
        serialize = SiwapModelSerializers(instance=siwap, many=True, context={'request': request})

        return JsonResponse({
            'siwap_data': serialize.data
        })

    def post(self, request):
        # 获取商品详情表单
        info_name = request.POST.get('info_name', None)

        if info_name:
            goods_info = GoodsInfoModel.objects.all()
            serialize = GoodsInfoModelSerializers(instance=goods_info, many=True)
            return JsonResponse({'data': serialize.data})
        else:
            goods = GoodsModel.objects.all()

            serialize = GoodsModelSerializers(instance=goods, many=True)
            return JsonResponse({'data': serialize.data})

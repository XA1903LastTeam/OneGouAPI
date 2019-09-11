from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from .api import SiwapModelSerializers, SiwapModel
from .api import GoodsModelSerializers, GoodsInfoModel, GoodsModel, GoodsInfoModelSerializers, GoodsImageModel, \
    GoodsImageSerializers
from Funy.api import CategoryModel


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


class GetCateGoodDataView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        zong_name = request.POST.get('yijifenleiming')
        er_name = request.POST.get('erjifenleiming')
        if not er_name or er_name == '全部':
            fruit = (CategoryModel.objects.get(name=zong_name)).goods_cate.all()
            serialize = GoodsModelSerializers(instance=fruit, many=True)

            return JsonResponse({'data': [{
                "commodityname":serialize.data.get('commodityname'),
                'commoditycode':serialize.data.get('commoditycode'),
                'maxlimitcount':serialize.data.get('maxlimitcount'),
                'originalprice':serialize.data.get('originalprice'),
            }]})
        else:
            fruit = (CategoryModel.objects.get((Q(name=er_name) & Q(father_id__name=zong_name)))).goods_cate.all()
            serialize = GoodsModelSerializers(instance=fruit, many=True)
            return JsonResponse({'data': serialize.data})


class GetGoodInfoView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        code = request.POST.get('goods_code')
        goods_code = GoodsInfoModel.objects.filter(goods_id__commoditycode=code).all()
        serialize = GoodsInfoModelSerializers(instance=goods_code, many=True)
        return JsonResponse({'data': serialize.data})

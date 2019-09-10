from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View


# Create your views here.
class GetHomeDataView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        # 该请求是根据地区来获取商品数据的，目前数据只有西安地区的数据，所以不需要考虑
        pass

    def post(self, request):
        pass

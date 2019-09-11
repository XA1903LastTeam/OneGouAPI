import io

from django.core.cache import cache
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from Address.models import AddressModel
from UserApp.models import UserModel
<<<<<<< HEAD
from .api import UserSeraLizer, AdderssSeraLizer
=======
from .api import UserSeraLizer
from CartList.models import OrderModel
>>>>>>> aa192591b084bdb5636d1ef477e2051227016f26


# Create your views here.
class UserAPIView(APIView):
    def get(self, request):
        datas = UserModel.objects.all()
        serializer = UserSeraLizer(datas, many=True)
        return JsonResponse({'data': serializer.data })


    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def post(self, request):
<<<<<<< HEAD
        phone = request.POST.get('phone', None)
        yan = request.POST.get('yanzhengma', None)
        if phone:
            if yan == cache.get('yanzhengma'):
                user = UserModel.objects.filter(phone=phone).first()
                user_data = UserSeraLizer(user)
                address = AdderssSeraLizer(AddressModel.objects.filter(user_id=user.id, state=True))
                # 将用户ID写入session
                request.session['user'] = user.id
                return JsonResponse({ 'user': user_data, 'address': address, 'msg': '登陆成功' })
            else:
                data = {
                    'msg': '验证码错误'
                }
                return JsonResponse(data)
        else:
            data = {
                'msg': '该手机号未注册'
            }
        return JsonResponse(data)
=======
        name = request.POST.get('name_id', None)
        print(name, type(name))
        datas = UserModel.objects.filter(id=name).first()
        serializer = UserSeraLizer(datas)
        return JsonResponse({ 'data':serializer.data })

class orderAPIView(View):
    def get(self,request):

        datas = OrderModel.objects.filter()
>>>>>>> aa192591b084bdb5636d1ef477e2051227016f26

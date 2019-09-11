import io

from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from UserApp.models import UserModel
from .api import UserSeraLizer


# Create your views here.
class UserAPIView(View):
    def get(self, request):
        datas = UserModel.objects.all()
        serializer = UserSeraLizer(datas, many=True)
        return JsonResponse({'data': serializer.data })


    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def post(self, request):
        name = request.POST.get('name_id', None)
        print(name, type(name))
        datas = UserModel.objects.filter(id=name).first()
        serializer = UserSeraLizer(datas)
        return JsonResponse({ 'data':serializer.data })






=======
        login = request.GET.get('login', None)
        if not login:
            datas = UserModel.objects.all()
            serializer = UserSeraLizer(datas, many=True)
>>>>>>> 7b59f841375f3e38557be03250363c5b0a942dd9

            return JsonResponse({'data': serializer.data})

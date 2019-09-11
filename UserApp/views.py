import io

from django.views import View
from django.http import JsonResponse

from UserApp.models import UserModel
from .api import UserSeraLizer


# Create your views here.
class UserAPIView(View):
    def get(self, request):
        login = request.GET.get('login', None)
        if not login:
            datas = UserModel.objects.all()
            serializer = UserSeraLizer(datas, many=True)
            return JsonResponse({'data': serializer.data})

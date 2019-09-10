import io

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer

from UserApp.models import UserModel
from .api import UserSeraLizer

# Create your views here.
class UserAPIView(APIView):

    def get(self, request):
        login = request.GET.get('login', None)
        if not login:
            datas = UserModel.objects.all()
            serializer = UserSeraLizer(datas, many=True)
            data = JSONRenderer().render(serializer.data)
            data = JSONParser().parse(io.BytesIO(data))

        return JsonResponse({'data': data})

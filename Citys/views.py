import io

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


from .api import CityModelsSerializers,CityAreaModelsSerializers



from .models import CityModels,CityAreaModels

class CityApi(View):
    def get(self,request):
        city_all = CityModels.objects.all()
        ser = CityModelsSerializers(city_all,many=True)
        return JsonResponse({'data':ser.data})

class CityAreaApi(View):
    def get(self,request):
        area_all = CityAreaModels.objects.all()
        ser = CityAreaModelsSerializers(area_all,many=True)
        return JsonResponse({'data':ser.data})

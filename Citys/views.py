from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .api import CityModelsSerializers



from .models import CityModels,CityAreaModels

# @api_view(['GET'])
def get_city(request):
    city_all = CityModels.objects.all()
    print(city_all)
    ser = CityModelsSerializers(city_all,many=True)
    print(ser.data)
    return Response(ser)

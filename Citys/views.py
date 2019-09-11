import io

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


from .api import CityModelsSerializers,CityAreaModelsSerializers



from .models import CityModels,CityAreaModels

class CityApi(View):
    def get(self,request):
        city_letter_set = []
        hot_city = CityModels.objects.filter(city_hot__gt=200).all()
        ser = CityModelsSerializers(hot_city,many=True)
        city_letter = CityModels.objects.values('city_letter').all()
        for i in range(len(city_letter)):
            city_letter_set.append(city_letter[i]['city_letter'])
        city_letter_set = set(city_letter_set)
        city_name = sorted(city_letter_set)
        print(city_name)
        for j in range(len(city_name)):
            city = CityModels.objects.filter(city_letter=city_name[j]).all()
            ser_city = CityModelsSerializers(city,many=True)
            city_name[j]= [ser_city.data]
        return JsonResponse({'data':{
                'hot_city':ser.data,
                'A':city_name[0],
                'B':city_name[1],
                'C':city_name[2],
                'D':city_name[3],
                'E':city_name[4],
                'F':city_name[5],
                'G':city_name[6],
                'H':city_name[7],
                'J':city_name[8],
                'K':city_name[9],
                'L':city_name[10],
                'M':city_name[11],
                'N':city_name[12],
                'P':city_name[13],
                'Q':city_name[14],
                'R':city_name[15],
                'S':city_name[16],
                'T':city_name[17],
                'W':city_name[18],
                'X':city_name[19],
                'Y':city_name[20],
                'Z':city_name[21],
        }})


class CityAreaApi(View):
    def get(self,request):
        a = request.GET.get('one_id',None)
        area_all = CityAreaModels.objects.filter(city_id=a).all()
        ser = CityAreaModelsSerializers(area_all,many=True)
        return JsonResponse({'data':ser.data})


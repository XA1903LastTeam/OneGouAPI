

from rest_framework import serializers
from .models import CityModels,CityAreaModels


class CityModelsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CityModels
        fields =('city_name',)
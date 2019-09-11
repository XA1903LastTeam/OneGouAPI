

from rest_framework import serializers
from .models import CityModels,CityAreaModels


class CityModelsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CityModels
        fields =('city_name', 'id')

class CityAreaModelsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CityAreaModels
        fields = ('cityareaname','id')
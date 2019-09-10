# -*- coding: utf-8 -*-
from .models import SiwapModel
from rest_framework import serializers
from Address.api import ActiveSerializer


class SiwapModelSerializers(serializers.ModelSerializer):
    active_id = ActiveSerializer

    class Meta:
        model = SiwapModel
        fields = ['active_id', 'active_img']

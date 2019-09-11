from rest_framework import serializers

from Funy.models import CategoryModel


class CategoryModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel

        fields = ['name', 'category_url','father_id']

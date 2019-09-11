

from rest_framework import serializers


from .models import CategoryModel


class CategorySerlaizer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('name','category_url','father_id')

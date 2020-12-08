from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, SubCategory, Links

"""
class LinkObjectRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value, Category):
            serializer = CategorySerializer(value)
        elif isinstance(value, SubCategory):
            serializer = SubCategorySerializer(value)
        else:
            raise Exception('Unexpected type of tagged object')

        return serializer.data
"""

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ['link_name', 'url']


class SubCategorySerializer(serializers.ModelSerializer):
    links = LinksSerializer(many=True, read_only = True)
    category_name = serializers.ReadOnlyField()
      
    class Meta:
        model = SubCategory
        exclude = ['category', 'id']


class CategorySerializer(serializers.ModelSerializer):
    links = LinksSerializer(many=True, read_only = True)
    sub_category = SubCategorySerializer(read_only = True, many = True)

    class Meta:
        model = Category
        exclude = ['id']




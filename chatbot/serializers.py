from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, SubCategory, Links

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ['link_name', 'url']
        


class SubCategorySerializer(serializers.ModelSerializer):
    links = LinksSerializer(many=True, read_only = True)
         
    class Meta:
        model = SubCategory
        exclude = ['category', 'id']


class CategorySerializer(serializers.ModelSerializer):
    sub_category = SubCategorySerializer(read_only = True, many = True)

    class Meta:
        model = Category
        exclude = ['id']





from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status

from chatbot.models import Category, Links, SubCategory
from chatbot.serializers import CategorySerializer, SubCategorySerializer, LinksSerializer


class CategoryList(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'category_name'


class LinkView(generics.RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        try: 
            category_name = kwargs['category_name']
            sub_category_name = kwargs['sub_category_name']
            link_name = kwargs['link_name']

        except KeyError:
            error_response = {'error': 'Something went Wrong! Couldn\'t resolve key in API'}
            return Response(data=error_response, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            category = Category.objects.get(category_name = category_name)
            sub_category = category.sub_category.all().get(sub_category_name = sub_category_name)
            link = sub_category.links.all().get(link_name = link_name)
            link_response = {'name' : link_name, 'url' : link.url}
            return Response(data = link_response, status= status.HTTP_200_OK)
        
        except (Category.DoesNotExist, SubCategory.DoesNotExist, Links.DoesNotExist):
            error_response = {'error': 'Invalid API'}
            return Response(data=error_response, status= status.HTTP_400_BAD_REQUEST)
        
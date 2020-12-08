
from rest_framework import viewsets
from chatbot.models import Category, Links, SubCategory
from chatbot.serializers import CategorySerializer
# Create your views here.

class CategoryList(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    #def get_queryset(self):
    #    return Category.objects.all()


"""    
class SubCategoryList(APIView):
   
    def get(self, request, format=None):
        sub_categories = SubCategory.objects.all()
        serializer = SubCategorySerializer(sub_categories, many=True)
        return Response(serializer.data)



class LinksList(APIView):
    
    def get(self, request, format=None):
        links = Links.objects.all()
        serializer = LinkObjectRelatedField(links, many=True)
        return Response(serializer.data)
        """
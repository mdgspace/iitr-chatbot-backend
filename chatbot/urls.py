from django.urls import include, path
from rest_framework import routers
from chatbot import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryList, basename='category-list')
#router.register(r'^sub-categories/$', views.SubCategoryList, basename='sub-category-list')
#router.register(r'links', views.LinksViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('sub-categories/', views.SubCategoryList.as_view()),
    #path('links/', views.LinksList.as_view())
]
from django.urls import include, path
from rest_framework import routers
from chatbot import views

router = routers.DefaultRouter()
router.register(r'chatbot', views.CategoryList, basename='Links')


urlpatterns = [
    path('', include(router.urls)),
    path('chatbot/<str:category_name>/<str:sub_category_name>/<str:link_name>', views.LinkView.as_view())
]
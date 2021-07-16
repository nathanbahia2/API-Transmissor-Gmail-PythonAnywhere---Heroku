from django.urls import path, include
from rest_framework import routers

from api import views


router = routers.DefaultRouter()
router.register('emails', views.EmailViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/conexoes', views.ConexaoViewSet.as_view()),
]

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('owners', views.OwnerViewSet)
router.register('events', views.EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
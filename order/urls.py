from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path, include
from .views import OrderViewSet, OrderItemViewSet

# Enter your urls here.

router = SimpleRouter()

router.register("order", OrderViewSet)
router.register("orderitem", OrderItemViewSet)

urlpatterns = [

]

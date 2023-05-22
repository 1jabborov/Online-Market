from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import ProviderViewSet

# Enter your urls here.

router = SimpleRouter()

router.register("provider", ProviderViewSet)


urlpatterns = [

]

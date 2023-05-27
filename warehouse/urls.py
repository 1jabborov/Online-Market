from rest_framework.routers import SimpleRouter
from .views import WarehouseProductViewSet

# Enter your urls here.

router = SimpleRouter()

router.register("warehouseproduct", WarehouseProductViewSet)



urlpatterns = [

]

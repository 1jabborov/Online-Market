from django.urls import path
from .views import OutlayCategoryViewSet, OutlayViewSet, PaymentTransactionViewSet
from rest_framework.routers import SimpleRouter

# Enter your urls here.

router = SimpleRouter()


router.register('outlaycategory', OutlayCategoryViewSet)
router.register('outlay', OutlayViewSet)
router.register('payment', PaymentTransactionViewSet)

urlpatterns = [

]

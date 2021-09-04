from .views import MarkViewSet, BrandViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('marks', MarkViewSet)
router.register('brands', BrandViewSet)

urlpatterns = []

urlpatterns += router.urls

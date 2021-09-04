from directory.serializers import MarkSerializer, BrandSerializer
from directory.models import Mark, Brand
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

class MarkViewSet(ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    permission_classes = [AllowAny, ]

class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [AllowAny, ]
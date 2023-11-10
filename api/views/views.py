from rest_framework import viewsets
from api.models.models import CategoryModels
from api.serializers.serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModels.objects.all()
    serializer_class = CategorySerializer
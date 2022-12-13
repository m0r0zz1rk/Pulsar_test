from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from products.models import Products
from products.serializers import ProductSerializer


class ProductsViewSet(viewsets.ReadOnlyModelViewSet):
    """Просмотр товаров"""
    serializer_class = ProductSerializer
    queryset = Products.objects.all()
    filter_backends = [DjangoFilterBackend,
                       SearchFilter]
    filterset_fields = ['status', ]
    search_fields = ['name', 'article']
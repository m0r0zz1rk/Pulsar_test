from django.urls import path

from products.api import ProductsViewSet

urlpatterns = [
    path('products/', ProductsViewSet.as_view({'get': 'list'})),
    path('product/<int:pk>', ProductsViewSet.as_view({'get': 'retrieve'}))
]
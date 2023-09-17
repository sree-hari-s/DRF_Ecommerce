from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Category, Product, Brand
from .serializers import CategorySerializer, ProductSerializer, BrandSerializer
# Create your views here.


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing categories.
    """
    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


# class BrandViewSet(viewsets.ViewSet):
#     """
#     A simple Viewset for viewing brands.
#     """
#     queryset = Brand.objects.all()

#     @extend_schema(responses=BrandSerializer)
#     def list(self, request):
#         serializer = BrandSerializer(self.queryset, many=True)
#         return Response(serializer.data)


# class ProductViewSet(viewsets.ViewSet):
#     """
#     A simple Viewset for viewing Products.
#     """
#     queryset = Product.objects.all()

#     @extend_schema(ProductSerializer)
#     def list(self, request):
#         serializer = ProductSerializer(self.queryset, many=True)
#         return Response(serializer.data)

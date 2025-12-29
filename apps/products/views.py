from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product
from .serializer import ProductSerializer

# Create your views here.


class ProductCRUD(APIView):

    def get(self, request, id=None):
        """ api to get products """
        if id:
            product = get_object_or_404(Product, id=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)

        products = Product.objects.all()
        return render(request, 'product.html', {
            'products': products
        })

    def post(self, request):
        """ api to add products """
        serializer = ProductSerializer(data=request.POST)

        if serializer.is_valid():
            serializer.save()
            return redirect('product-page')

        products = Product.objects.all()
        return render(request, 'product.html', {
            'products': products,
            'errors': serializer.errors
        })

    def put(self, request, id):
        """ Update product (API) """
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """ Delete product """
        product = get_object_or_404(Product, id=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer
# Create your views here.

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    return Response({'message': 'Welcome to Django REST framework api'})


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # default query look is 'pk'

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description') or None
        
        if description is None:
            description = name
        serializer.save(description=description)


product_list_create_view = ProductListCreateAPIView.as_view()


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_retrieve_view = ProductRetrieveAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description')

        if description is None:
            description = name
        
        serializer.save(description=description)
    

product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_destroy_view = ProductDestroyAPIView.as_view()


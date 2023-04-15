from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics
from rest_framework import permissions, authentication

from .models import Product
from .serializers import ProductSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    return Response({'message': 'Welcome to Django REST framework api'})


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication,
    authentication.SessionAuthentication]

    
    # default query lookup is 'pk'

    # override get_queryset to filter the search.
    # Here, we are filtering products based on user
    # def get_queryset(self, *args, **kwargs):
    #     query = super().get_queryset(*args, **kwargs)
    #     user = self.request.user
    #     result = Product.objects.none()
    #     print("USer", user)
    #     if user.is_authenticated:
    #       result = query.filter(user=user)
    #     return result

    # We can override this method of CreateListAPIView
    # Though these are not required.
    # def get(self, request, *args, **kwargs):
    #     print("======= Executing GET method ... ")
    #     instance = Product.objects.all().filter(user=request.user)
    #     data = []
    #     if instance is not None:
    #         data = ProductSerializer(instance=instance, many=True).data
    #         # Use many=True to indicate that multiple objects are being serialized
    #     return Response(data)
    
    # def post(self, request, *args, **kwargs):
    #     #return super().post(request, *args, **kwargs)
    #     print("========= POST ==============")
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         instance = serializer.save(user=request.user)
    #         print("instance", instance)
    #         data = serializer.data
    #         print(data)
    #     return Response(data)

    # override from CreateModelMixin
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description') or None
        # getting current logged in user
        user = self.request.user
        price = serializer.validated_data.get('price')   
        if description is None:
            description = name
        serializer.save(description=description, user=user)


product_list_create_view = ProductListCreateAPIView.as_view()


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_retrieve_view = ProductRetrieveAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

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
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


product_destroy_view = ProductDestroyAPIView.as_view()


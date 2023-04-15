
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/', obtain_auth_token, name='api_token_auth'),
    path('admin/', admin.site.urls),
    path('api/products/', include('products.urls')),
    path('api/search/', include('search.urls')),
]
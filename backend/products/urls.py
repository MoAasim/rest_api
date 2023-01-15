from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_list_create_view),
    path('<int:pk>/', views.product_retrieve_view),
    path('update/<int:pk>/', views.product_update_view),
    path('delete/<int:pk>/', views.product_destroy_view),
    path('', views.api_home),
]
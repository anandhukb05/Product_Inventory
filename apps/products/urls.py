from django.urls import path
from .views import ProductCRUD

urlpatterns = [
    path('products/', ProductCRUD.as_view(), name='product-page'),
    path('products/<int:id>/', ProductCRUD.as_view(), name='product-detail'),
]

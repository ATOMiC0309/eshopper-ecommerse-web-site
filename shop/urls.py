from django.urls import path
from .views import index, shop, product_by_category, detail, filter_by, product_update, product_delete

urlpatterns = [
    path('', index, name="index"),
    path('shop/', shop, name="shop"),
    path('product-by/<int:category_pk>/', product_by_category, name="product_by_category"),
    path('product-detail/<int:product_pk>/', detail, name="detail"),
    path('sort-by/<str:filter_key>/', filter_by, name="filter_by"),
    path('update/<int:pk>/', product_update, name="update"),
    path('delete/<int:pk>/', product_delete, name="delete"),
]

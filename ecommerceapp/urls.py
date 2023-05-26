from django.urls import path
from . import views

app_name = 'ecommerceapp'
urlpatterns = [
    path('', views.allProductsCategory, name = 'allProductsCategory'),
    path('<slug:c_slug>/', views.allProductsCategory, name = 'products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.productCategoryDetail, name='productCategoryDetail')
]

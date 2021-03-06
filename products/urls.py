from django.urls import path
from products import views


urlpatterns = [
    path('', views.index, name='index'),
    path('store/', views.StoreListView.as_view(), name='store'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
]
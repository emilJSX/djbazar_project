from django.urls import path,re_path,include
from .views import contact_view,ProductCreate, ProductDetailView, CategoryDetailView,HomeView,TopProductDetailView,reklama

app_name = 'djstore'


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('advertising/', reklama, name="reklama"),
    path('contact/',contact_view,name='contact'),
    path('create/', ProductCreate.as_view(), name="product"),
    path('description/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('top-description/<int:pk>/', TopProductDetailView.as_view(), name='top-product-detail'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    
] 

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductView.as_view(), name='index'),
    path('category/<str:type>', views.CategoryDetailView.as_view(), name='category'),
    path('register/', views.Register.as_view(), name='register'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('order/', views.OrderCreateView.as_view(), name='order'),
    path('product/<int:id>', views.get_post, name='getpost'),
    path('category/get/<int:id>', views.get_category, name='getcategory'),
    path('contact/<int:id>/', views.ContactView.as_view(), name='contact'),
    path('home/', views.home, name='home'),
]



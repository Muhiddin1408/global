from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductView.as_view(), name='index'),
    # path('jihozlar/', views.JihozlarView.as_view(), name='jihozlar'),
    path('category/<str:type>', views.CategoryDetailView.as_view(), name='category'),
    # path('post/', views.PostView.as_view(), name='post'),
    # path('create/', views.PostCreateView.as_view(), name='create-post'),
    path('product/<int:id>', views.get_post, name='getpost'),
    path('category/get/<int:id>', views.get_category, name='getcategory'),
    # path('jihoz/get/<int:id>', views.get_jihoz, name='getjihoz'),
    # path('jihoz_buyurtma/get/<int:id>/', views.post_jihoz_buyurtma, name='buyurtma'),
    path('contact/<int:id>', views.ContactView.as_view(), name='contact'),
]



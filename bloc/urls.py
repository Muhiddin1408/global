from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('jihozlar/', views.JihozlarView.as_view(), name='jihozlar'),
    path('post/', views.PostView.as_view(), name='post'),
    path('create/', views.PostCreateView.as_view(), name='create-post'),
    path('post/get/<int:id>', views.get_post, name='getpost'),
    path('category/get/<int:id>', views.get_category, name='getcategory'),
    path('jihoz/get/<int:id>', views.get_jihoz, name='getjihoz'),
    path('jihoz_buyurtma/get/<int:id>/', views.post_jihoz_buyurtma, name='buyurtma'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]

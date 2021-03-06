from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('charts/club/', views.ClubChartView.as_view(), name='charts'),
    path('widgets/', views.WidgetsView.as_view(), name='widgets'),
    path('order/user/<int:id>/', views.orderUserView, name='orderuser'),
    path('delivering/<int:id>/', views.deliveringView, name='delivering'),
    path('completed/<int:id>/', views.completedView, name='completed'),
    path('notcompleted/<int:id>/', views.notcompletedView, name='notcompleted'),
    path('tables/', views.TablesView.as_view(), name='tables'),
    path('user/<int:id>/', views.UserEditForm.as_view(), name='useredit'),
    path('products/', views.ProductView.as_view(), name='products'),
    path('products/<int:id>/', views.ProductEditView.as_view(), name='productedit'),
    path('products/add/', views.AddProductView.as_view(), name='addproduct'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
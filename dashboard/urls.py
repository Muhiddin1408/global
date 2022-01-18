from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('charts/club/', views.ClubChartView.as_view(), name='charts'),
    path('widgets/', views.WidgetsView.as_view(), name='widgets'),
    path('order/user/<int:id>/', views.orderUserView, name='orderuser'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
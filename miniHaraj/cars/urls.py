from django.urls import path
from . import views

urlpatterns = [
  path('',views.views_home,name='views_home'),
  path('create/',views.create_views,name='create_views'),
  path('details/<int:car_id>/', views.car_detail_view, name='car_detail'),
  path('update/<int:car_id>/', views.car_update_view, name='car_update'),
  path('delete/<int:car_id>/', views.car_delete_view, name='car_delete'),
  path('all/',views.all_views, name='all_views'),
  
]
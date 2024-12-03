from django.urls import path,include
from . import views

urlpatterns = [
   path('brandcreate/', views.create_brand, name='create_brand'),
    path('brands/', views.brand_some, name='brand_list'),
    path('brands/<int:brand_id>/', views.brand_page, name='brand_details'),  
]
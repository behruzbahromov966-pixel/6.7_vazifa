from django.urls import path

from .views import index, detail, car_by_brand

urlpatterns =[
    path('', index, name='index'),
    path('car/<int:car_id>/', detail, name='detail'),
    path('brand/<int:brand_id>/', car_by_brand, name='car_by_brand')
]
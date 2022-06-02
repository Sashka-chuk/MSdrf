from django.urls import path
from .views import *

urlpatterns = [
    path('', layout),
    path('city/', CityListView.as_view(), name='city'),
    path('city/<int:city_id>/street/', StreetViewSet.as_view(), name='street'),
    path('shop/', ShopView.as_view(), name='getshop'),
    path('shop/create', ShopCreateView.as_view(), name='postshop')
]

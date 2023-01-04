from django.urls import path
from .views import SubproductoView


urlpatterns = [
    path('api/subproductos/',SubproductoView.as_view(),name='subproductos'),
    path('api/subproductos/<int:id>',SubproductoView.as_view(),name='subproductos_id'),
]
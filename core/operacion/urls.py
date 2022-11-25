from django.urls import path
from .views import OperacionView,SubproductoView


urlpatterns = [
    path('api/operaciones/',OperacionView.as_view(),name='operaciones'),
    path('api/subproductos/',SubproductoView.as_view(),name='subproductos'),
    path('api/subproductos/<int:id>',SubproductoView.as_view(),name='subproductos_id'),
]
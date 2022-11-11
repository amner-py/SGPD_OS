from django.urls import path
from .views import OperacionView


urlpatterns = [
    path('api/operaciones/',OperacionView.as_view(),name='operaciones'),
]
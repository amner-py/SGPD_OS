from django.urls import path
from .views import SeccionView

urlpatterns = [
    path('secciones',SeccionView.as_view(),name='secciones'),
]
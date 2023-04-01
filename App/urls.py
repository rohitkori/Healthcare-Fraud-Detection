from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.predictor, name = 'predictor'),
    path('', views.index, name = 'index'),
]
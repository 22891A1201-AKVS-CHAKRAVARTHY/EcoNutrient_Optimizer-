from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_crop_yield, name='predict_crop_yield'),  # Root URL now loads the prediction page
]

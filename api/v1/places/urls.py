from django.urls import path
from api.v1.places import views


urlpatterns = [
    path('', views.places),
]
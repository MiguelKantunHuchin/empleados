from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.IndexView.as_view()),
    path("home/lista", views.PruebaListView.as_view()),
    path("home/add", views.PruebaCreateView.as_view(), name="prueba"),
]

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView

from applications.home.models import Prueba
from .forms import PruebaForm


# Create your views here.
class IndexView(TemplateView):
    template_name = "home/home.html"


class PruebaListView(ListView):
    template_name = "home/lista.html"
    queryset = ["A", "B", "C"]  # type: ignore
    context_object_name = "listaPrueba"


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = "/"

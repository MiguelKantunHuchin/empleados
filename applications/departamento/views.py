from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView

from applications.persona.models import Empleado
from .forms import NewDepartamentoForm
from .models import Departamento

# Create your views here.


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = "departamentos"  #!El context sirve para renombrar la variable por defecto object_list


class NewDepartamento(FormView):
    template_name = "departamento/new_departamento.html"
    form_class = NewDepartamentoForm
    success_url = "/"

    def form_valid(self, form):

        depa = Departamento(
            name=form.cleaned_data["departamento"],
            shor_name=form.cleaned_data["shorname"],
        )

        depa.save()

        nombre = form.cleaned_data["nombre"]
        apellidos = form.cleaned_data["apellidos"]
        Empleado.objects.create(
            first_name=nombre, last_name=apellidos, job="3", departamento=depa
        )
        return super(NewDepartamento, self).form_valid(form)

from django.forms import BaseModelForm
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
from .models import Empleado


# Create your views here.


class InicioView(TemplateView):
    template_name = "inicio.html"


# Mostrar todos los empleados
class ListAllEmpleados(ListView):
    template_name = "persona/list_all.html"
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.get("keyword", "")
        lista = Empleado.objects.filter(full_name__icontains=palabra_clave)

        return lista


class ListEmpleadosAdmin(ListView):
    template_name = "persona/list_empleados.html"
    paginate_by = 10
    ordering = "id"
    model = Empleado


# Filtrar empleados por area de la empresa
class ListEmleadoByArea(ListView):
    template_name = "persona/lista_por_area.html"

    def get_queryset(self):
        area = self.kwargs["shorname"]
        lista = Empleado.objects.filter(departamento__shor_name=area)
        return lista


# Filtrar empleados por trabajo


# Filtrar empleados por palabra clave
class ListEmpleadoByKeyword(ListView):
    template_name = "persona/by_keyword.html"
    context_object_name = "empleados"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("keyword", "")
        lista = Empleado.objects.filter(first_name=palabra_clave)

        return lista


# Filtrar empleados por habilidades
class ListHabilidadesEmpleado(ListView):

    # def obtenerEmpleados(self):
    #     model = Empleado
    #     return Empleado.first_name

    template_name = "persona/habilidades_empleado.html"
    model = Empleado
    context_object_name = "habilidades"

    def get_queryset(self):
        empleado = Empleado.objects.get(id=4)
        return empleado.habilidades.all()


# Details View


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detalles_empleado.html"


# TemplateView
class SuccessView(TemplateView):
    template_name = "persona/success.html"


# CreateView


class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    fields = [
        "first_name",
        "last_name",
        "job",
        "departamento",
        "habilidades",
        "picture",
    ]
    success_url = reverse_lazy("persona_app:empleados_admin")

    # Cuando el formulario es correcto, se ejecuta esto
    def form_valid(self, form: BaseModelForm):

        # Aqui va la logica, para en este caso concatenar nombre y apellido
        # Asignamos el registro guardado en la DB a una variable
        empleado = form.save(
            commit=False
        )  # El commit false se pone para que no genere un guardado

        # Accedemos al atributo full_name y concatenamos para crear el nombre completo
        empleado.full_name = empleado.first_name + " " + empleado.last_name

        # Guardamos los cambios para que se refleje en la base de datos
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


# UpdateView


class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = ["first_name", "last_name", "job", "departamento", "habilidades"]
    success_url = reverse_lazy("persona_app:empleados_admin")


# DeleteView


class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html"
    model = Empleado
    success_url = reverse_lazy("persona_app:empleados_admin")

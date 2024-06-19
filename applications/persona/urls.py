from django.urls import path
from . import views


app_name = "persona_app"

urlpatterns = [
    path("lista-todos-empleados", views.ListAllEmpleados.as_view()),
    path("lista-empleados-by-area/<shorname>", views.ListEmleadoByArea.as_view()),
    path("buscar-empleado/", views.ListEmpleadoByKeyword.as_view()),
    path("habilidades-empleado/", views.ListHabilidadesEmpleado.as_view()),
    path("ver-empleado/<pk>/", views.EmpleadoDetailView.as_view()),
    path("agregar-empleado/", views.EmpleadoCreateView.as_view()),
    path("success/", views.SuccessView.as_view(), name="correcto"),
    path(
        "editar-empleado/<pk>/", views.EmpleadoUpdateView.as_view(), name="actualizar"
    ),
    path(
        "eliminar-empleado/<pk>/", views.EmpleadoDeleteView.as_view(), name="eliminar"
    ),
]

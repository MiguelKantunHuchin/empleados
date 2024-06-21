from django.urls import path
from . import views


app_name = "persona_app"

urlpatterns = [
    path("", views.InicioView.as_view(), name="inicio"),
    path(
        "lista-todos-empleados", views.ListAllEmpleados.as_view(), name="empleados_all"
    ),
    path(
        "lista-empleados-by-area/<shorname>",
        views.ListEmleadoByArea.as_view(),
        name="empleados_area",
    ),
    path(
        "lista-empleados-admin/",
        views.ListEmpleadosAdmin.as_view(),
        name="empleados_admin",
    ),
    path("buscar-empleado/", views.ListEmpleadoByKeyword.as_view()),
    path("habilidades-empleado/", views.ListHabilidadesEmpleado.as_view()),
    path("ver-empleado/<pk>/", views.EmpleadoDetailView.as_view(), name="detalles"),
    path("agregar-empleado/", views.EmpleadoCreateView.as_view(), name="empleado_add"),
    path("success/", views.SuccessView.as_view(), name="correcto"),
    path(
        "editar-empleado/<pk>/", views.EmpleadoUpdateView.as_view(), name="actualizar"
    ),
    path(
        "eliminar-empleado/<pk>/", views.EmpleadoDeleteView.as_view(), name="eliminar"
    ),
]

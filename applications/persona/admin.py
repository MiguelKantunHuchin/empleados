from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.

admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("id","last_name", "first_name", "departamento", "job", "codigo_empleado")

    def codigo_empleado(self, obj):
        return (
            str(obj.first_name[0:2]).upper()
            + str(obj.last_name[0:2]).upper()
            + "_"
            + obj.departamento.shor_name
        )

    search_fields = ("first_name",)
    list_filter = ("job", "habilidades")
    filter_horizontal = ("habilidades",)


admin.site.register(Empleado, EmpleadoAdmin)

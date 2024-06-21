from django.db import models
from applications.departamento.models import Departamento


class Habilidades(models.Model):
    habilidad = models.CharField("Habilidad", max_length=50)

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades de Empleados"

    def __str__(self):
        return str(self.id) + "-" + self.habilidad  # type: ignore


# Create your models here.
class Empleado(models.Model):

    JOB_CHOICES = (
        ("0", "Contador"),
        ("1", "Administrador"),
        ("2", "Economista"),
        ("3", "Otros"),
    )
    first_name = models.CharField("Nombres", max_length=60)
    last_name = models.CharField("Apellidos", max_length=60)
    full_name = models.CharField("Nombre Completo", max_length=120, blank=True)
    job = models.CharField("Trabajo", choices=JOB_CHOICES, max_length=1)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    picture = models.ImageField("Foto", upload_to="empleado", blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades, blank=True)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ["last_name"]
        unique_together = ("first_name", "last_name")

    def __str__(self):
        return str(self.id) + "-" + self.last_name + "-" + self.first_name + "-" + self.departamento.shor_name  # type: ignore

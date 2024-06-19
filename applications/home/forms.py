from django import forms

from .models import Prueba


class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields = ["titulo", "subtitulo", "cantidad"]
        #El widgets sirve para cambiar los atributos de los campos
        widgets ={
            'titulo' : forms.TextInput(
                attrs= {
                    'placeholder' : 'Ingrese un título aquí'
                }
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data["cantidad"]
        if cantidad < 1:
            raise forms.ValidationError("Tiene que er mayor a 1 we")

        return cantidad

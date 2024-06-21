from django import forms

#Creamos un form pero que no sea de modelForm, sino uno simple
class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField( max_length=50, required=False)
    departamento = forms.CharField( max_length=50, required=False)
    shorname = forms.CharField( max_length=20, required=False)
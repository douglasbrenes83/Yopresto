from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'cedula', 'direccion', 'edad', 'sexo', 'telefono', 'foto', 'descripcion']

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        # Agregar clases a los campos
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['cedula'].widget.attrs.update({'class': 'form-control'})
        self.fields['direccion'].widget.attrs.update({'class': 'form-control'})
        self.fields['edad'].widget.attrs.update({'class': 'form-control'})
        self.fields['sexo'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefono'].widget.attrs.update({'class': 'form-control'})
        self.fields['foto'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control'})



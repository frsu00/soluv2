from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Localizacion, Categoria, Producto, Reclamo, ProductoImage

class UserForm(UserCreationForm):
    # django.contrib.auth.User attributes
    first_name = forms.CharField(max_length=150, required=False)
    last_name = forms.CharField(max_length=150, required=False)
    email = forms.EmailField(max_length=150)

    # Profile attributes
    documento_identidad = forms.CharField(max_length=8)
    fecha_nacimiento = forms.DateField()
    estado = forms.CharField(max_length=3)
    ## Opciones de genero
    MASCULINO = 'MA'
    FEMENINO = 'FE'
    NO_BINARIO = 'NB'
    GENERO_CHOICES = [
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
        (NO_BINARIO, 'No Binario')
    ]
    genero = forms.ChoiceField(choices=GENERO_CHOICES)

    # Cliente attributes
    is_cliente = forms.BooleanField(required=False)
    preferencias = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=False)

    # Colaborador attributes
    is_colaborador = forms.BooleanField(required=False)
    reputacion = forms.FloatField(required=False)
    cobertura_entrega = forms.ModelChoiceField(queryset=Localizacion.objects.all(), required=False)

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'documento_identidad',
                  'fecha_nacimiento',
                  'estado',
                  'genero',
                  'is_cliente',
                  'preferencias',
                  'is_colaborador',
                  'reputacion',
                  'cobertura_entrega',
                  ]
        help_texts = {
                    'username': None,
                    'password1': None,
                    'password2': None,
                }


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'proveedor': forms.HiddenInput()
        }


class ImageForm(ModelForm):
    class Meta:
        model = ProductoImage
        fields = '__all__'
        widgets = {
            'product': forms.HiddenInput()
        }


class ReclamoForm(ModelForm):
    class Meta:
        model = Reclamo
        fields = '__all__'
        widgets = {
            'cliente': forms.HiddenInput()
        }
        help_texts = {
            'cliente': None,
            'proveedor': None,
        }

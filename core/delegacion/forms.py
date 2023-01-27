from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Usuario

class UsuarioChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model=Usuario
        

class UsuarioCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=Usuario

class PerfilUsuarioForm(forms.ModelForm):
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese su contraseña',
            'id':'password1',
            'required':'required'
        }
    ))
    password2=forms.CharField(label='Confirmar contraseña',widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese nuevamente su contraseña',
            'id':'password2',
            'required':'required'
        }
    ))

    class Meta:
        model=Usuario
        fields=('first_name','last_name','username','email','fecha_nacimiento')
        widgets={
            'first_name':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese sus nombres'
                }
            ),
            'last_name':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese sus apellidos'
                }
            ),
            'username':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre de usuario'
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'ejemplo@mail.com'
                }
            ),
            'fecha_nacimiento':forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class':'form-control',
                    'placeholder':'DD-MM-AAAA',
                    'type':'date'
                }
            ),
        }
    
    def clean_password2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden.')
        return password2

    def save(self, commit=True):
        form=super()
        data={}
        try:
            if form.is_valid():
                pwd=self.cleaned_data['password1']
                user=form.save(commit=False)
                if user.pk is None:
                    user.set_password(pwd)
                else:
                    user_u=Usuario.objects.get(pk=user.pk)
                    if user_u.password != pwd:
                        user.set_password(pwd)
                user.save()
            else:
                data['error']=form.errors
        except Exception as e:
            data['error']=str(e)
        return user
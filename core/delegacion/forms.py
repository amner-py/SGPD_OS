from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Delegacion


class DelegacionChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model=Delegacion
        

class DelegacionCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=Delegacion
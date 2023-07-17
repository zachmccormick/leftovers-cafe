from django.forms import ModelForm

from app.inventory.models import Leftovers


class LeftoversForm(ModelForm):
    class Meta:
        model = Leftovers
        fields = ['title', 'subtitle', 'details', 'price']

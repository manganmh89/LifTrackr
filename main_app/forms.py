from django.forms import ModelForm
from .models import Feeding

class LoggingForm(ModelForm):
    class Meta:
        model = Logging
        fields = ('__all__')
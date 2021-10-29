from django.forms import ModelForm
from app.models import Ingressos


# Create the form class.
class IngressosForm(ModelForm):
    class Meta:
        model = Ingressos
        fields = ['evento', 'tipo', 'qtde', 'pagamento']

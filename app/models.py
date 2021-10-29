from django.db import models

# Create your models here.

from django.db import models


# Create your models here.
class Ingressos(models.Model):
    evento = models.CharField(max_length=150)
    tipo = models.CharField(max_length=150)
    qtde = models.IntegerField()
    pagamento = models.IntegerField()

from django.db import models


class Cedula(models.Model):

    TIPO_CEDULA = [
        ('ELECTRONICA', 'Electrónica'),
        ('PAPEL', 'Papel'),
    ]

    numero_expediente = models.CharField(
        max_length=20
    )

    caratula = models.CharField(
        max_length=80
    )

    tipo_cedula = models.CharField(
        max_length=20,
        choices=TIPO_CEDULA
    )

    fecha = models.DateField()

    observaciones = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Cédula {self.id} - {self.numero_expediente}"
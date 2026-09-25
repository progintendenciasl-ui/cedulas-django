from django.db import models


class Expediente(models.Model):

    numero = models.CharField(
        max_length=20
    )

    caratula = models.CharField(
        max_length=80
    )

    fecha_inicio = models.DateField(
        blank=True,
        null=True
    )

    fecha = models.DateField(
        blank=True,
        null=True
    )

    observaciones = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.numero} - {self.caratula}"


class Audiencia(models.Model):

    expediente = models.ForeignKey(
        Expediente,
        on_delete=models.CASCADE,
        related_name='audiencias'
    )

    fecha = models.DateField()

    hora = models.TimeField()

    tipo = models.CharField(
        max_length=80,
        blank=True,
        null=True
    )

    estado = models.CharField(
        max_length=80,
        blank=True,
        null=True
    )

    resultado = models.CharField(
        max_length=80,
        blank=True,
        null=True
    )

    observaciones = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Audiencia {self.fecha} - {self.expediente.numero}"


class Cedula(models.Model):

    TIPO_CEDULA = [
        ('ELECTRONICA', 'Electrónica'),
        ('PAPEL', 'Papel'),
    ]

    numero_cedula = models.CharField(
        max_length=20,
        unique=True
    )

    expediente = models.ForeignKey(
    Expediente,
    on_delete=models.CASCADE,
    related_name='cedulas'
    )   

    notificoparte = models.CharField(
        max_length=40
    )

    tipo_cedula = models.CharField(
        max_length=20,
        choices=TIPO_CEDULA
    )

    fecha = models.DateField(
        null=True,
        blank=True
    )

    observaciones = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Cédula {self.numero_cedula}"
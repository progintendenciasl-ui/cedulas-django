from django.contrib import admin

from .models import Expediente, Audiencia, Cedula
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


@admin.register(Expediente)
class ExpedienteAdmin(admin.ModelAdmin):

    list_display = ('numero', 'caratula', 'observaciones')

    search_fields = ('caratula', 'numero')

    class Media:
        js = ('admin/js/live_search.js',)


@admin.register(Audiencia)
class AudienciaAdmin(admin.ModelAdmin):

    list_display = (
        'expediente',
        'fecha',
        'hora',
        'tipo',
        'estado',
    )

    autocomplete_fields = ['expediente']
    date_hierarchy = 'fecha'
    ordering = ['fecha']


def exportar_pdf(modeladmin, request, queryset):

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        'attachment; filename="cedulas.pdf"'
    )

    pdf = SimpleDocTemplate(response)

    datos = [
        [
            'N° Cedula',
            'Expediente',
            'Parte Notificada',
            'Tipo',
            'Fecha'
        ]
    ]

    for cedula in queryset:

        datos.append([
            cedula.numero_cedula,
            str(cedula.expediente),
            cedula.notificoparte,
            cedula.tipo_cedula,
            cedula.fecha.strftime('%d/%m/%Y')
            if cedula.fecha else ''
        ])

    tabla = Table(datos)

    tabla.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
    ]))

    pdf.build([tabla])

    return response


exportar_pdf.short_description = (
    "Generar PDF de cédulas seleccionadas"
)

@admin.register(Cedula)
class CedulaAdmin(admin.ModelAdmin):

    actions = [exportar_pdf]

    list_display = (
        'numero_cedula',
        'expediente',
        'notificoparte',
        'tipo_cedula',
        'fecha',
    )

    search_fields = (
        'numero_cedula',
        'notificoparte',
        'expediente__caratula',
        'expediente__numero',
    )

    autocomplete_fields = ['expediente']

admin.site.site_header = "Sistema de Cédulas"
admin.site.site_title = "Relaciones Laborales"
admin.site.index_title = "Panel de Administración"
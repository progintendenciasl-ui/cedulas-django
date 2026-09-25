from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect

from cedulas.views import (
    abrir_reporte_cedulas,
    reporte_cedulas,
    reporte_cedulas_pdf,
    reporte_audiencias,
    reporte_audiencias_pdf,
)

def inicio(request):
    return redirect('/admin/')

urlpatterns = [

    path('', inicio),

    path('admin/', admin.site.urls),
    
    path(
    'reportes/audiencias/',
    reporte_audiencias,
    name='reporte_audiencias'
),
    path(
    'reportes/audiencias/pdf/',
    reporte_audiencias_pdf,
    name='reporte_audiencias_pdf'
),

    path(
        'reporte-cedulas/',
        abrir_reporte_cedulas,
        name='admin_reporte_cedulas'
    ),

    path(
        'reportes/cedulas/',
        reporte_cedulas,
        name='reporte_cedulas'
    ),

    path(
        'reportes/cedulas/pdf/',
        reporte_cedulas_pdf,
        name='reporte_cedulas_pdf'
    ),
]
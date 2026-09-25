from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib import colors
from django.shortcuts import render
from .models import Cedula
from django.shortcuts import redirect
from .models import Audiencia

def abrir_reporte_cedulas(request):
    return redirect('/reportes/cedulas/')


def reporte_cedulas(request):

    cedulas = Cedula.objects.all()

    desde = request.GET.get('desde')
    hasta = request.GET.get('hasta')
    parte = request.GET.get('parte')
    fecha_desde = request.GET.get('fecha_desde')
    fecha_hasta = request.GET.get('fecha_hasta')

    if desde:
        cedulas = cedulas.filter(numero_cedula__gte=desde)

    if hasta:
        cedulas = cedulas.filter(numero_cedula__lte=hasta)

    if parte:
        cedulas = cedulas.filter(
            notificoparte__icontains=parte
        )

    if fecha_desde:
        cedulas = cedulas.filter(
            fecha__gte=fecha_desde
        )

    if fecha_hasta:
        cedulas = cedulas.filter(
            fecha__lte=fecha_hasta
        )

    return render(
        request,
        'cedulas/reporte_cedulas.html',
        {
            'cedulas': cedulas
        }
    )
    
def reporte_cedulas_pdf(request):

    cedulas = Cedula.objects.all()

    desde = request.GET.get('desde')
    hasta = request.GET.get('hasta')
    parte = request.GET.get('parte')
    fecha_desde = request.GET.get('fecha_desde')
    fecha_hasta = request.GET.get('fecha_hasta')

    if desde:
        cedulas = cedulas.filter(numero_cedula__gte=desde)

    if hasta:
        cedulas = cedulas.filter(numero_cedula__lte=hasta)

    if parte:
        cedulas = cedulas.filter(notificoparte__icontains=parte)

    if fecha_desde:
        cedulas = cedulas.filter(fecha__gte=fecha_desde)

    if fecha_hasta:
        cedulas = cedulas.filter(fecha__lte=fecha_hasta)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cedulas.pdf"'

    pdf = SimpleDocTemplate(response)

    datos = [
        ['N°', 'Expediente', 'Parte', 'Tipo', 'Fecha']
    ]

    for c in cedulas:
        datos.append([
            c.numero_cedula,
            str(c.expediente),
            c.notificoparte,
            c.tipo_cedula,
            c.fecha.strftime('%d/%m/%Y') if c.fecha else ''
        ])

    tabla = Table(datos)

    pdf.build([tabla])

    return response

def reporte_audiencias(request):

    audiencias = Audiencia.objects.all().order_by('fecha')

    expediente = request.GET.get('expediente')
    tipo = request.GET.get('tipo')
    fecha_desde = request.GET.get('fecha_desde')
    fecha_hasta = request.GET.get('fecha_hasta')

    if expediente:
        audiencias = audiencias.filter(
            expediente__caratula__icontains=expediente
        )

    if tipo:
        audiencias = audiencias.filter(
            tipo__icontains=tipo
        )

    if fecha_desde:
        audiencias = audiencias.filter(
            fecha__gte=fecha_desde
        )

    if fecha_hasta:
        audiencias = audiencias.filter(
            fecha__lte=fecha_hasta
        )

    return render(
        request,
        'cedulas/reporte_audiencias.html',
        {'audiencias': audiencias}
    )
    
def reporte_audiencias_pdf(request):

    audiencias = Audiencia.objects.all().order_by('fecha')

    expediente = request.GET.get('expediente')
    tipo = request.GET.get('tipo')
    fecha_desde = request.GET.get('fecha_desde')
    fecha_hasta = request.GET.get('fecha_hasta')

    if expediente:
        audiencias = audiencias.filter(
            expediente__caratula__icontains=expediente
        )

    if tipo:
        audiencias = audiencias.filter(
            tipo__icontains=tipo
        )

    if fecha_desde:
        audiencias = audiencias.filter(
            fecha__gte=fecha_desde
        )

    if fecha_hasta:
        audiencias = audiencias.filter(
            fecha__lte=fecha_hasta
        )

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        'attachment; filename="audiencias.pdf"'
    )

    pdf = SimpleDocTemplate(response)

    datos = [[
        'Expediente',
        'Fecha',
        'Hora',
        'Tipo',
        'Estado'
    ]]

    for a in audiencias:

        datos.append([
            str(a.expediente),
            a.fecha.strftime('%d/%m/%Y') if a.fecha else '',
            str(a.hora) if a.hora else '',
            a.tipo or '',
            a.estado or '',
        ])

    tabla = Table(datos)

    pdf.build([tabla])

    return response
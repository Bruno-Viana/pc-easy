from django import template

register = template.Library()

@register.filter
def nome_format_tera(value):
    return value.replace("PLACA DE VÍDEO","")

@register.filter
def nome_format_pichau(value):
    return value.replace("Placa de Video","")

@register.filter
def nome_format_kabum(value):
    return value.replace("Placa de Vídeo","")

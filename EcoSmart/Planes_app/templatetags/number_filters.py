from django import template
import locale

register = template.Library()

@register.filter
def spanish_number(value):
    """Formatea números al estilo español: 1.000.000,00"""
    try:
        # Convertir a float si es string
        if isinstance(value, str):
            value = float(value)
        
        # Formatear con separadores españoles
        formatted = f"{value:,.2f}"
        # Cambiar punto por coma para decimales y coma por punto para miles
        formatted = formatted.replace(',', 'TEMP').replace('.', ',').replace('TEMP', '.')
        return formatted
    except (ValueError, TypeError):
        return value
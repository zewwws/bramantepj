from urllib.parse import quote

from django.conf import settings

# Override any key via COMPANY = {...} in settings.
DEFAULT_COMPANY = {
    'name': 'Bramante',
    'tagline': 'Atunci cînd lucrul devine artă',
    'phone': '079 222 792',
    'phone_intl': '+37379222792',
    'email': '',  # TODO: add the company e-mail when available
    'address': 'Str. Ioana Radu 29, mun. Chișinău, Republica Moldova',
    'hours': 'Luni–Vineri 08:00–17:00 · Sâmbătă 09:00–13:00',  # TODO: confirm opening hours
    'facebook': 'https://www.facebook.com/www.bramante.md',
}


def company(request):
    data = {**DEFAULT_COMPANY, **getattr(settings, 'COMPANY', {})}
    digits = data['phone_intl'].lstrip('+')
    data['whatsapp'] = f'https://wa.me/{digits}'
    data['viber'] = f'viber://chat?number=%2B{digits}'
    data['map_embed'] = f'https://www.google.com/maps?q={quote(data["address"])}&output=embed'
    data['map_link'] = f'https://www.google.com/maps/search/?api=1&query={quote(data["address"])}'
    return {'company': data}

from django.db import migrations

PRODUCTS = [
    {
        'name': 'Ferestre din PVC',
        'slug': 'ferestre-pvc',
        'category': 'ferestre',
        'material': 'pvc',
        'icon': 'window',
        'short_description': 'Ferestre termoizolante la comandă, cu profile multicameră și geam dublu sau triplu.',
        'description': (
            'Ferestrele din PVC sunt alegerea cea mai răspândită pentru case și apartamente: '
            'izolează bine termic și fonic, nu necesită întreținere specială și au un raport foarte bun '
            'între preț și performanță.\n\n'
            'Le producem la dimensiunea exactă a golului, în variante fixe, cu deschidere simplă, '
            'oscilo-batantă sau basculantă, în alb sau în culori și decoruri imitație lemn.'
        ),
        'features': (
            'Profile multicameră pentru izolare termică ridicată\n'
            'Geam termoizolant dublu sau triplu\n'
            'Feronerie oscilo-batantă cu închidere în mai multe puncte\n'
            'Culori și decoruri imitație lemn la alegere\n'
            'Opțional: rulouri, plase de insecte, glafuri'
        ),
        'order': 10,
    },
    {
        'name': 'Ferestre din aluminiu',
        'slug': 'ferestre-aluminiu',
        'category': 'ferestre',
        'material': 'aluminiu',
        'icon': 'window',
        'short_description': 'Profile subțiri și rezistente, cu rupere de punte termică, pentru suprafețe vitrate mari.',
        'description': (
            'Aluminiul permite ferestre cu profile mai subțiri și suprafețe vitrate mai mari, '
            'fiind foarte rezistent și stabil în timp. Este potrivit pentru locuințe moderne, birouri '
            'și clădiri comerciale.\n\n'
            'Folosim sisteme cu rupere de punte termică, astfel încât ferestrele din aluminiu să izoleze '
            'eficient, iar vopsirea în câmp electrostatic permite orice culoare din paleta RAL.'
        ),
        'features': (
            'Sisteme cu rupere de punte termică\n'
            'Profile subțiri, mai multă lumină naturală\n'
            'Rezistență mare și durată lungă de viață\n'
            'Vopsire în orice culoare RAL\n'
            'Potrivite pentru deschideri mari'
        ),
        'order': 20,
    },
    {
        'name': 'Uși din PVC',
        'slug': 'usi-pvc',
        'category': 'usi',
        'material': 'pvc',
        'icon': 'door',
        'short_description': 'Uși de intrare, de balcon și de terasă, izolate termic și sigure.',
        'description': (
            'Ușile din PVC sunt o soluție practică pentru intrarea în casă, balcon sau terasă. '
            'Oferă izolare bună, etanșeitate și o gamă largă de modele: cu panouri pline, cu geam '
            'sau combinate.\n\n'
            'Le echipăm cu balamale și feronerie de siguranță, yale cu cilindru și, la cerere, cu '
            'sisteme de închidere în mai multe puncte.'
        ),
        'features': (
            'Uși de intrare, balcon și terasă\n'
            'Panouri pline, vitrate sau combinate\n'
            'Închidere în mai multe puncte\n'
            'Prag redus pentru acces ușor'
        ),
        'order': 30,
    },
    {
        'name': 'Uși din aluminiu',
        'slug': 'usi-aluminiu',
        'category': 'usi',
        'material': 'aluminiu',
        'icon': 'door',
        'short_description': 'Uși robuste pentru locuințe, blocuri, magazine și clădiri publice.',
        'description': (
            'Ușile din aluminiu sunt alese acolo unde contează rezistența la trafic intens: intrări de '
            'bloc, spații comerciale, birouri și clădiri publice, dar și locuințe cu design modern.\n\n'
            'Le realizăm cu sau fără rupere de punte termică, cu amortizoare, bare antipanică, '
            'yale electromagnetice și alte accesorii, în funcție de destinație.'
        ),
        'features': (
            'Rezistență ridicată la uzură\n'
            'Variante cu rupere de punte termică\n'
            'Accesorii: amortizoare, bare antipanică, interfon\n'
            'Orice culoare RAL'
        ),
        'order': 40,
    },
    {
        'name': 'Uși și sisteme glisante',
        'slug': 'sisteme-glisante',
        'category': 'usi',
        'material': 'pvc-aluminiu',
        'icon': 'sliding',
        'short_description': 'Deschideri largi către terasă sau grădină, fără să ocupe spațiu.',
        'description': (
            'Sistemele glisante și glisant-culisante permit deschideri mari către terasă sau grădină, '
            'fără ca foile ușii să ocupe spațiu în cameră.\n\n'
            'Le producem atât din PVC, cât și din aluminiu, cu geam termoizolant și feronerie '
            'care asigură o manevrare ușoară chiar și pentru foi mari.'
        ),
        'features': (
            'Deschideri largi, fără spațiu ocupat în interior\n'
            'Variante din PVC sau aluminiu\n'
            'Manevrare ușoară și etanșare bună\n'
            'Ideale pentru terase și living-uri'
        ),
        'order': 50,
    },
    {
        'name': 'Fațade și pereți cortină',
        'slug': 'fatade-pereti-cortina',
        'category': 'constructii',
        'material': 'aluminiu',
        'icon': 'facade',
        'short_description': 'Fațade vitrate din aluminiu pentru clădiri de birouri, comerciale și rezidențiale.',
        'description': (
            'Pereții cortină din aluminiu și sticlă dau clădirilor un aspect modern și aduc multă '
            'lumină naturală în interior.\n\n'
            'Proiectăm, producem și montăm fațade vitrate pentru clădiri de birouri, centre comerciale, '
            'showroom-uri și locuințe, adaptate proiectului arhitectural.'
        ),
        'features': (
            'Sisteme de fațadă din aluminiu cu izolare termică\n'
            'Geam termoizolant, securizat sau laminat\n'
            'Integrare cu ferestre și uși în fațadă\n'
            'Execuție după proiectul arhitectural'
        ),
        'order': 60,
    },
    {
        'name': 'Verande și terase închise',
        'slug': 'verande-terase',
        'category': 'constructii',
        'material': 'pvc-aluminiu',
        'icon': 'veranda',
        'short_description': 'Spații luminoase, folosite tot anul, din aluminiu sau PVC.',
        'description': (
            'O verandă sau o terasă închisă transformă un spațiu exterior într-o cameră luminoasă, '
            'pe care o puteți folosi în orice anotimp.\n\n'
            'Realizăm structuri din aluminiu sau PVC, cu pereți fixi, glisanți sau pliabili, '
            'adaptate casei, restaurantului sau cafenelei dumneavoastră.'
        ),
        'features': (
            'Structuri din aluminiu sau PVC\n'
            'Pereți fixi, glisanți sau pliabili\n'
            'Potrivite pentru case, restaurante și cafenele\n'
            'Proiectare la dimensiunea spațiului'
        ),
        'order': 70,
    },
    {
        'name': 'Închideri de balcoane',
        'slug': 'inchideri-balcoane',
        'category': 'constructii',
        'material': 'pvc-aluminiu',
        'icon': 'balcony',
        'short_description': 'Balcoane închise cu PVC sau aluminiu, pentru un spațiu în plus în locuință.',
        'description': (
            'Închiderea balconului adaugă practic o cameră în plus: un spațiu protejat de vânt, '
            'ploaie și praf, cu izolare termică mai bună pentru întregul apartament.\n\n'
            'Folosim tâmplărie din PVC sau aluminiu, cu deschideri clasice sau glisante, '
            'în funcție de forma balconului și de buget.'
        ),
        'features': (
            'Tâmplărie din PVC sau aluminiu\n'
            'Deschideri clasice sau glisante\n'
            'Parapet și glafuri la cerere\n'
            'Izolare termică și fonică îmbunătățită'
        ),
        'order': 80,
    },
]


def seed(apps, schema_editor):
    Product = apps.get_model('br_main', 'Product')
    for data in PRODUCTS:
        Product.objects.update_or_create(slug=data['slug'], defaults=data)


def unseed(apps, schema_editor):
    Product = apps.get_model('br_main', 'Product')
    Product.objects.filter(slug__in=[p['slug'] for p in PRODUCTS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('br_main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]

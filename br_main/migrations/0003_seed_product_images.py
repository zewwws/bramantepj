from django.db import migrations

# Photos committed under media/products/. Only fills products that have no
# image yet, so photos uploaded through the admin are never overwritten.
IMAGES = {
    'ferestre-pvc': 'products/ferestre-pvc.jpg',
    'usi-pvc': 'products/usi-pvc.jpg',
    'usi-aluminiu': 'products/usi-aluminiu.jpg',
    'verande-terase': 'products/veranda-pvc.jpg',
    'inchideri-balcoane': 'products/balcoane-pvc.jpg',
}


def seed_images(apps, schema_editor):
    Product = apps.get_model('br_main', 'Product')
    for slug, path in IMAGES.items():
        Product.objects.filter(slug=slug, image='').update(image=path)


class Migration(migrations.Migration):

    dependencies = [
        ('br_main', '0002_seed_products'),
    ]

    operations = [
        migrations.RunPython(seed_images, migrations.RunPython.noop),
    ]

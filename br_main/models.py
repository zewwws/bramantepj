from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('ferestre', 'Ferestre'),
        ('usi', 'Uși'),
        ('constructii', 'Construcții din aluminiu și PVC'),
    ]
    MATERIAL_CHOICES = [
        ('pvc', 'PVC'),
        ('aluminiu', 'Aluminiu'),
        ('pvc-aluminiu', 'PVC și aluminiu'),
    ]
    ICON_CHOICES = [
        ('window', 'Fereastră'),
        ('door', 'Ușă'),
        ('facade', 'Fațadă'),
        ('veranda', 'Verandă'),
        ('sliding', 'Glisant'),
        ('balcony', 'Balcon'),
    ]

    name = models.CharField('denumire', max_length=120)
    slug = models.SlugField(unique=True)
    category = models.CharField('categorie', max_length=20, choices=CATEGORY_CHOICES)
    material = models.CharField('material', max_length=20, choices=MATERIAL_CHOICES)
    icon = models.CharField(
        'pictogramă', max_length=20, choices=ICON_CHOICES, default='window',
        help_text='Afișată când produsul nu are imagine.',
    )
    short_description = models.CharField('descriere scurtă', max_length=255)
    description = models.TextField('descriere', help_text='Paragrafele se separă printr-un rând liber.')
    features = models.TextField('caracteristici', blank=True, help_text='O caracteristică pe fiecare rând.')
    image = models.FileField(
        'imagine', upload_to='products/', blank=True,
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])],
    )
    order = models.PositiveIntegerField('ordine', default=0)
    is_published = models.BooleanField('publicat', default=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'produs'
        verbose_name_plural = 'produse'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('br_main:product_detail', args=[self.slug])

    def feature_list(self):
        return [line.strip() for line in self.features.splitlines() if line.strip()]


class ContactRequest(models.Model):
    name = models.CharField('nume', max_length=120)
    phone = models.CharField('telefon', max_length=40)
    email = models.EmailField('e-mail', blank=True)
    product = models.ForeignKey(
        Product, verbose_name='produs de interes', on_delete=models.SET_NULL, null=True, blank=True,
    )
    message = models.TextField('mesaj')
    created_at = models.DateTimeField('primit la', auto_now_add=True)
    is_handled = models.BooleanField('rezolvat', default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'cerere de contact'
        verbose_name_plural = 'cereri de contact'

    def __str__(self):
        return f'{self.name} ({self.created_at:%d.%m.%Y})'

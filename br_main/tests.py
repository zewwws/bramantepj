from django.test import TestCase
from django.urls import reverse

from .models import ContactRequest, Product


class PageTests(TestCase):
    def test_public_pages_render(self):
        for name in ['home', 'product_list', 'about', 'contact']:
            with self.subTest(page=name):
                response = self.client.get(reverse(f'br_main:{name}'))
                self.assertEqual(response.status_code, 200)

    def test_seeded_products_listed(self):
        response = self.client.get(reverse('br_main:product_list'))
        self.assertContains(response, 'Ferestre din PVC')
        self.assertContains(response, 'Fațade și pereți cortină')

    def test_product_detail(self):
        product = Product.objects.get(slug='ferestre-pvc')
        response = self.client.get(product.get_absolute_url())
        self.assertContains(response, product.name)
        self.assertContains(response, 'Geam termoizolant dublu sau triplu')

    def test_unpublished_product_hidden(self):
        product = Product.objects.get(slug='ferestre-pvc')
        product.is_published = False
        product.save()
        response = self.client.get(product.get_absolute_url())
        self.assertEqual(response.status_code, 404)


class ContactFormTests(TestCase):
    def test_valid_submission_is_saved(self):
        product = Product.objects.get(slug='usi-aluminiu')
        response = self.client.post(reverse('br_main:contact'), {
            'name': 'Ion Popescu',
            'phone': '0700 000 000',
            'email': '',
            'product': product.pk,
            'message': 'Ușă de intrare, aproximativ 100x210 cm.',
        }, follow=True)
        self.assertContains(response, 'Vă mulțumim')
        request = ContactRequest.objects.get()
        self.assertEqual(request.product, product)

    def test_missing_fields_show_errors(self):
        response = self.client.post(reverse('br_main:contact'), {'name': '', 'phone': '', 'message': ''})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(ContactRequest.objects.exists())

    def test_product_preselected_from_query(self):
        response = self.client.get(reverse('br_main:contact') + '?produs=verande-terase')
        product = Product.objects.get(slug='verande-terase')
        self.assertContains(response, f'value="{product.pk}" selected')

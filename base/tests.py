from django.test import TestCase

# Create your tests here.
class UnitTests(TestCase):
    
    def test_can_get_home(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_get_about(self):
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'about.html')

    def test_can_get_products(self):
        response = self.client.get('/products/')
        self.assertTemplateUsed(response, 'products.html')

    def test_can_get_contact(self):
        response = self.client.get('/contact/')
        self.assertTemplateUsed(response, 'contact.html')

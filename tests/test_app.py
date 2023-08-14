import unittest
from flask import Flask
from app.routes import api

class TestCurrencyConverter(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(api)
        self.client = self.app.test_client()

    def test_get_currency_rates(self):
        response = self.client.get('/currency_rates')
        self.assertEqual(response.status_code, 200)

    def test_get_currency_rate(self):
        response = self.client.get('/currency_rates/USD')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'USD', response.data)  # Verifica que la respuesta contenga 'USD'

    def test_get_nonexistent_currency_rate(self):
        response = self.client.get('/currency_rates/XYZ')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Currency rate for XYZ not found', response.data)

    def test_get_transactions_by_currency(self):
        response = self.client.get('/transactions/USD')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'T2006', response.data)  # Verifica que la respuesta contenga 'T2006'

    def test_get_transactions_by_sku_and_currency(self):
        response = self.client.get('/transactions/T2006/USD')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'T2006', response.data)  # Verifica que la respuesta contenga 'T2006'

    def test_get_nonexistent_transactions_by_sku_and_currency(self):
        response = self.client.get('/transactions/XYZ/USD')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'No transactions found for SKU XYZ and currency USD', response.data)

if __name__ == '__main__':
    unittest.main()

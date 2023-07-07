import json
from rest_framework import status
from django.urls import reverse
from django.test import TestCase, Client

from cryptocurrency.models import Cryptocurrency
from api.serializers import CryptoSerializer


client = Client()


class GetCryptoListApiTest(TestCase):
    """ Test for GET CryptoList from API """

    def setUp(self):
        # Creating Cryptocurrency test objects
        Cryptocurrency.objects.create(
            name='Bitcoin', symbol='BTC', price=50000.0, percent_change_1h=1.0, percent_change_24h=1.0, percent_change_7d=1.0, volume=100000000, market_cap=500000000)
        Cryptocurrency.objects.create(
            name='Ethereum', symbol='ETH', price=2000.0, percent_change_1h=2.0, percent_change_24h=2.0, percent_change_7d=2.0, volume=50000000, market_cap=200000000)

    def test_get_all_cryptocurrencies(self):
        # API GET Response
        response = client.get(reverse('crypto_list'))

        # Load from DB
        cryptocurrencies = Cryptocurrency.objects.all()
        serializer = CryptoSerializer(cryptocurrencies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PostCryptoListApiTest(TestCase):
    """ Test for POST CryptoList API """

    def setUp(self):
        # Test payloads (valid/invalid)
        self.valid_payload = {
            "name": "Dogecoin",
            "symbol": "DOGE",
            "price": 0.05,
            "percent_change_1h": 5.0,
            "percent_change_24h": 5.0,
            "percent_change_7d": 5.0,
            "volume": 1000000,
            "market_cap": 50000000
        }
        self.invalid_payload = {
            "name": "",
            "symbol": "",
            "price": 0.05,
            "percent_change_1h": 5.0,
            "percent_change_24h": 5.0,
            "percent_change_7d": 5.0,
            "volume": 1000000,
            "market_cap": 50000000
        }

    def test_create_valid_cryptocurrency(self):
        # API Post valid data
        response = client.post(
            reverse('crypto_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_cryptocurrency(self):
        # API Post invalid data
        response = client.post(
            reverse('crypto_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetCryptoDetailApiTest(TestCase):
    """ Test for GET CryptoDetail API """

    def setUp(self):
        # Test symbols
        self.valid_symbol = 'BTC'
        self.invalid_symbol = 'ETH'

        # Creating Cryptocurrency test objects
        Cryptocurrency.objects.create(
            name='Bitcoin', symbol=self.valid_symbol, price=50000.0, percent_change_1h=1.0, percent_change_24h=1.0, percent_change_7d=1.0, volume=100000000, market_cap=500000000)

    def test_valid_get_detail(self):
        # API Get response valid
        response = client.get(
            reverse('crypto_detail', kwargs={'symbol': self.valid_symbol}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_get_detail(self):
        # API Get response invalid
        response = client.get(
            reverse('crypto_detail', kwargs={'symbol': self.invalid_symbol})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class PostCryptoDetailApiTest(TestCase):
    """ Test for POST CryptoDetail API """

    def setUp(self):
        # Test symbols
        self.symbol = 'BTC'

        # Creating Cryptocurrency test objects
        Cryptocurrency.objects.create(
            name='Bitcoin', symbol=self.symbol, price=50000.0, percent_change_1h=1.0, percent_change_24h=1.0, percent_change_7d=1.0, volume=100000000, market_cap=500000000)

        # Test payloads (valid/invalid)
        self.valid_payload = {
            "name": "Dogecoin",
            "symbol": "DOGE",
            "price": 0.05,
            "percent_change_1h": 5.0,
            "percent_change_24h": 5.0,
            "percent_change_7d": 5.0,
            "volume": 1000000,
            "market_cap": 50000000
        }
        self.invalid_payload = {
            "name": "",
            "symbol": "",
            "price": 0.05,
            "percent_change_1h": 5.0,
            "percent_change_24h": 5.0,
            "percent_change_7d": 5.0,
            "volume": 1000000,
            "market_cap": 50000000
        }

    def test_create_valid_detail_cryptocurrency(self):
        # API Post response valid
        response = client.post(
            reverse('crypto_detail', kwargs={'symbol': self.symbol}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_detail_cryptocurrency(self):
        # API Post response invalid
        response = client.post(
            reverse('crypto_detail', kwargs={'symbol': self.symbol}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PutCryptoDetailApiTest(TestCase):
    """ Test for PUT CryptoDetail API """

    def setUp(self):
        # Test symbols
        self.symbol = 'BTC'
        self.invalid_symbol = 'ETH'

        # Creating Cryptocurrency test objects
        Cryptocurrency.objects.create(
            name='Bitcoin', symbol=self.symbol, price=50000.0, percent_change_1h=1.0, percent_change_24h=1.0, percent_change_7d=1.0, volume=100000000, market_cap=500000000)

        # Test payloads (valid/invalid)
        self.valid_payload = {
            "name": "Dogecoin",
            "symbol": "DOGE",
            "price": 0.05,
            "percent_change_1h": 5.0,
            "percent_change_24h": 5.0,
            "percent_change_7d": 5.0,
            "volume": 1000000,
            "market_cap": 50000000
        }
        self.invalid_payload = {
            "name": "",
            "symbol": "",
            "price": 0.05,
            "percent_change_1h": 5.0,
            "percent_change_24h": 5.0,
            "percent_change_7d": 5.0,
            "volume": 1000000,
            "market_cap": 50000000
        }

    def test_put_valid_detail_cryptocurrency(self):
        # API Put response valid
        response = client.put(
            reverse('crypto_detail', kwargs={'symbol': self.symbol}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_invalid_detail_cryptocurrency(self):
        # API Put response invalid
        response = client.put(
            reverse('crypto_detail', kwargs={'symbol': self.symbol}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_get_invalid_detail_cryptocurrency(self):
        # API Get response invalid
        response = client.put(
            reverse('crypto_detail', kwargs={'symbol': self.invalid_symbol}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class PatchCryptoDetailApiTest(TestCase):
    """ Test for PATCH CryptoDetail API """

    def setUp(self):
        # Test symbols
        self.symbol = 'BTC'
        self.invalid_symbol = 'ETH'

        # Creating Cryptocurrency test objects
        Cryptocurrency.objects.create(
            name='Bitcoin', symbol=self.symbol, price=50000.0, percent_change_1h=1.0, percent_change_24h=1.0, percent_change_7d=1.0, volume=100000000, market_cap=500000000)

        # Test payloads (valid/invalid)
        self.valid_payload = {
            'market_cap': 200,
        }
        self.invalid_payload = {
            'market_cap': 'TEST',
        }

    def test_patch_valid_detail_cryptocurrency(self):
        # API Patch response valid
        response = client.patch(
            reverse('crypto_detail', kwargs={'symbol': self.symbol}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_invalid_detail_cryptocurrency(self):
        # API Patch response invalid
        response = client.patch(
            reverse('crypto_detail', kwargs={'symbol': self.symbol}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_get_invalid_detail_cryptocurrency(self):
        # API Get response invalid
        response = client.patch(
            reverse('crypto_detail', kwargs={'symbol': self.invalid_symbol}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class DeleteCryptoDetailApiTest(TestCase):
    """" Test for DELETE CryptoDetail API """

    def setUp(self):
        # Creating Cryptocurrency test objects
        Cryptocurrency.objects.create(
            name='Bitcoin', symbol='BTC', price=50000.0, percent_change_1h=1.0, percent_change_24h=1.0, percent_change_7d=1.0, volume=100000000, market_cap=500000000)

    def test_delete_valid_cryptocurrency(self):
        # Load from DB
        cryptocurrency = Cryptocurrency.objects.get(symbol='BTC')

        # API Delete response valid
        response = client.delete(
            reverse('crypto_detail', kwargs={
                    'symbol': cryptocurrency.symbol}),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_cryptocurrency(self):
        # API Delete response invalid
        response = client.delete(
            reverse('crypto_detail', kwargs={'symbol': 'ETH'})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

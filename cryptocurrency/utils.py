import requests

from .models import Cryptocurrency, News


def update_cryptocurrency_info():
    """
    Updating Cryptocurrencies in database from CoinMarketCapAPI request.
    """
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '9d90c40a-3445-418b-8373-067bd1886961',
    }
    parameters = {
        'limit': 300,
    }

    response = requests.get(
        url=url, headers=headers, params=parameters).json()

    data = response.get('data')
    for currency_data in data:
        cryptocurrency_queryset = Cryptocurrency.objects.filter(
            name=currency_data.get('name'), symbol=currency_data.get('symbol')
        )
        if cryptocurrency_queryset.exists():
            cryptocurrency = cryptocurrency_queryset.first()
        else:
            cryptocurrency = Cryptocurrency.objects.create(
                name=currency_data.get('name'),
                symbol=currency_data.get('symbol'),
                price=round(currency_data.get(
                    'quote').get('USD').get('price'), 2),
                percent_change_1h=round(currency_data.get(
                    'quote').get('USD').get('percent_change_1h'), 2),
                percent_change_24h=round(currency_data.get(
                    'quote').get('USD').get('percent_change_24h'), 2),
                percent_change_7d=round(currency_data.get(
                    'quote').get('USD').get('percent_change_7d'), 2),
                volume=round(currency_data.get(
                    'quote').get('USD').get('volume_24h')),
                market_cap=round(currency_data.get(
                    'quote').get('USD').get('market_cap')),
            )


def update_news():
    """
    Updating news in database from NewsAPI request.
    """
    url = 'https://newsapi.org/v2/everything'
    headers = {
        'X-Api-Key': 'e7c231a538b34d9b9c8196446cc57738',
    }
    parameters = {
        'q': 'криптовалюты',
        'language': 'ru',
    }
    response = requests.get(url=url, headers=headers, params=parameters).json()
    data = response.get('articles')
    for news_data in data:
        news = News.objects.get_or_create(
            title=news_data.get('title'),
            author=news_data.get('author'),
            defaults={
                'description': news_data.get('description'),
                'url': news_data.get('url'),
                'url_to_image': news_data.get('urlToImage'),
                'published_at': news_data.get('publishedAt'),
            }
        )[0]
        news.description = news_data.get('description')
        news.url = news_data.get('url')
        news.url_to_image = news_data.get('urlToImage')
        news.published_at = news_data.get('publishedAt')
        news.save()

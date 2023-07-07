from django.db import models
from django.contrib.auth.models import User


class Cryptocurrency(models.Model):
    """
    This model represents a cryptocurrency. 
    Used to store and retrieve information about cryptocurrencies.

    Fields:
        name: name of the cryptocurrency.
        symbol: symbol code of the cryptocurrency.
        price: current price of the cryptocurrency.
        percent_change_1h: change in the price of the cryptocurrency over the last 1 hour.
        percent_change_24h: change in the price of the cryptocurrency over the last 24 hours.
        percent_change_7d: change in the price of the cryptocurrency over the last 7 days.
        volume: trading volume of the cryptocurrency.
        market_cap: market capitalization of the cryptocurrency.
    """
    name = models.CharField(max_length=255, verbose_name='Название')
    symbol = models.CharField(max_length=50, verbose_name='Символьный код')
    price = models.DecimalField(
        max_digits=20, decimal_places=2, verbose_name='Текущий курс')
    percent_change_1h = models.DecimalField(
        max_digits=20, decimal_places=2, verbose_name='1ч %')
    percent_change_24h = models.DecimalField(
        max_digits=20, decimal_places=2, verbose_name='24ч %')
    percent_change_7d = models.DecimalField(
        max_digits=20, decimal_places=2, verbose_name='7д %')
    volume = models.DecimalField(
        max_digits=20, decimal_places=0, verbose_name='Объем торгов')
    market_cap = models.DecimalField(
        max_digits=20, decimal_places=0, verbose_name='Рыночная капитализация')

    class Meta:
        verbose_name = 'Криптовалюта'
        verbose_name_plural = 'Криптовалюты'

    def __str__(self):
        return self.name


class FavoriteCryptocurrency(models.Model):
    """
    This model represents a user favorite's cryptocurrency.
    Used to store and retrieve information about user favorite cryptocurrency.
    Realizes Many-to-Many relationship between User and Cryptocurrency models.

    Fields:
        user: foreign key to User model.
        cryptocurrency: foreign key to Cryptocurrency model.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cryptocurrency = models.ForeignKey(
        Cryptocurrency, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'cryptocurrency')


class News(models.Model):
    """
    This model represents an article.
    Used to store and retrieve information about news.

    Fields:
        title: title of the article.
        author: author of the article.
        description: description of the article.
        url: URL to original article.
        url_to_image: URL to picture in article.
        published_at: when article was published.
    """
    title = models.CharField(max_length=255, verbose_name='Название')
    author = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Автор')
    description = models.TextField(
        null=True, blank=True, verbose_name='Описание')
    url = models.URLField(verbose_name='URL новости')
    url_to_image = models.URLField(
        null=True, blank=True, verbose_name='URL картинки')
    published_at = models.DateTimeField(verbose_name='Время публикации')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Cryptocurrency, FavoriteCryptocurrency, News
from .utils import update_cryptocurrency_info, update_news


def index_view(request):
    """
    A view that displays a list of cryptocurrencies and a list of the user's favorite cryptocurrencies (if the user is authenticated).
    List of cryptocurrencies is obtained from the database. In this View, the update_cryptocurrency_info() function is called,
    which loads actual data into the database through CoinMarketAPI.

    Args:
        request: HTTP request object.

    Returns:
        Response object containing rendered HTML template.
    """
    update_cryptocurrency_info()
    crypto_list = Cryptocurrency.objects.all().distinct()

    if request.user.is_authenticated:
        favorite_cryptos = FavoriteCryptocurrency.objects.filter(
            user=request.user).values('cryptocurrency')
        crypto_ids = [favorite_crypto['cryptocurrency']
                      for favorite_crypto in favorite_cryptos]
        favorites_list = Cryptocurrency.objects.filter(id__in=crypto_ids)
        context = {
            'crypto_list': crypto_list,
            'favorites_list': favorites_list,
        }
        return render(request, 'index.html', context)

    return render(request, 'index.html', {'crypto_list': crypto_list})


def search_cryptocurrency(request):
    """
    This view processes a GET request and searches for cryptocurrencies based on a user-defined query.

    Args:
        request: HTTP request object.

    Returns:
        Response object containing rendered HTML template.
    """
    query = request.GET.get('q')
    cryptocurrencies = Cryptocurrency.objects.filter(
        Q(name__icontains=query) | Q(symbol__icontains=query))
    return render(request, 'search.html', {'query': query, 'crypto_list': cryptocurrencies})


@login_required()
def add_to_favorite(request, crypto_id):
    """
    View allows logged in users to add a cryptocurrency to their list of favorites.

    Args:
        request: HTTP request object.
        crypto_id: primary key from Cryptocurrency object.

    Returns:
        Redirect object which redirects user to 'index' page
    """
    cryptocurrency = get_object_or_404(Cryptocurrency, pk=crypto_id)
    FavoriteCryptocurrency.objects.create(
        user=request.user, cryptocurrency=cryptocurrency)
    return redirect('cryptocurrency:index')


@login_required()
def remove_from_favorites(request, crypto_id):
    """
    View allows logged in users to remove a cryptocurrency from their list of favorites.

    Args:
        request: HTTP request object.
        crypto_id: primary key from Cryptocurrency object.

    Returns:
        Redirect object which redirects user to 'index' page
    """
    cryptocurrency = get_object_or_404(Cryptocurrency, pk=crypto_id)
    favorite_cryptocurrency = FavoriteCryptocurrency.objects.get(
        user=request.user, cryptocurrency=cryptocurrency)
    favorite_cryptocurrency.delete()
    return redirect('cryptocurrency:index')


@login_required()
def favorites_list(request):
    """
    View allows logged in users to watch their list of favorites.

    Args:
        request: HTTP request object.

    Returns:
        Response object containing rendered HTML template.
    """
    favorite_cryptocurrencies = FavoriteCryptocurrency.objects.filter(
        user=request.user).values('cryptocurrency')
    crypto_ids = [favorite_crypto['cryptocurrency']
                  for favorite_crypto in favorite_cryptocurrencies]
    favorites_list = Cryptocurrency.objects.filter(id__in=crypto_ids)
    context = {
        'favorites_list': favorites_list,
    }
    return render(request, 'favorites_list.html', context)


def news_list(request):
    """
    View which displays a list of news items and data about them. 
    The news is loaded from the database, the data is fed into the database through the update_news() function.

    Args:
        request: HTTP request object.

    Returns:
        Response object containing rendered HTML template.
    """
    update_news()
    news_list = News.objects.all()
    return render(request, 'news.html', {'news_list': news_list})

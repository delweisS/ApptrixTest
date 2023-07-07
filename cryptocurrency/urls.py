from django.urls import path

from .views import index_view, search_cryptocurrency, add_to_favorite, remove_from_favorites, favorites_list, news_list

app_name = 'cryptocurrency'
urlpatterns = [
    # Index page (List of all cryptocurrencies)
    path('', index_view, name='index'),

    # Search page
    path('search/', search_cryptocurrency, name='search'),

    # Favorites cryptos (list, add, remove)
    path('favorites/', favorites_list, name='favorites_list'),
    path('add_favorite/<int:crypto_id>/', add_to_favorite, name='add_favorite'),
    path('remove_favorite/<int:crypto_id>/',
         remove_from_favorites, name='remove_favorite'),

    # News page
    path('news/', news_list, name='news'),
]

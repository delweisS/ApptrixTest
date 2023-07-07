from django.urls import path

from .views import CryptoList, CryptoDetail

urlpatterns = [
    # Cryptocurrency detail info
    path('<str:symbol>/', CryptoDetail.as_view(), name="crypto_detail"),

    # List of all cryptocurrencies
    path('', CryptoList.as_view(), name="crypto_list"),
]

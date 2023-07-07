from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Cryptocurrency, News


class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'price', 'volume', 'market_cap')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


admin.site.register(Cryptocurrency, CryptocurrencyAdmin)
admin.site.register(News, NewsAdmin)
admin.site.unregister(Group)

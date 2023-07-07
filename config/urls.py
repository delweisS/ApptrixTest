from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin panel
    path('admin/', admin.site.urls),

    # User accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),

    # API
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # Local
    path('', include('cryptocurrency.urls')),
]

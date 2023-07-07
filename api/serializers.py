from rest_framework import serializers

from cryptocurrency.models import Cryptocurrency


class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = '__all__'

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CryptoSerializer
from cryptocurrency.models import Cryptocurrency


class CryptoList(generics.ListCreateAPIView):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptoSerializer


class CryptoDetail(APIView):
    def get_object(self, symbol):
        try:
            return Cryptocurrency.objects.filter(symbol=symbol).first()
        except Cryptocurrency.DoesNotExist:
            return None

    def get(self, request, symbol):
        cryptocurrency = self.get_object(symbol)
        if cryptocurrency:
            serializer = CryptoSerializer(cryptocurrency)
            return Response(serializer.data)
        else:
            return Response({'message': 'Cryptocurrency not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, symbol):
        serializer = CryptoSerializer(data=request.data)
        if serializer.is_valid():
            cryptocurrency = Cryptocurrency.objects.create(
                name=serializer.validated_data['name'],
                symbol=serializer.validated_data['symbol'],
                price=serializer.validated_data['price'],
                percent_change_1h=serializer.validated_data['percent_change_1h'],
                percent_change_24h=serializer.validated_data['percent_change_24h'],
                percent_change_7d=serializer.validated_data['percent_change_7d'],
                volume=serializer.validated_data['volume'],
                market_cap=serializer.validated_data['market_cap'],
            )
            return Response({'message': 'Cryptocurrency created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, symbol):
        cryptocurrency = self.get_object(symbol)
        if cryptocurrency:
            serializer = CryptoSerializer(
                cryptocurrency, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Cryptocurrency updated successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Cryptocurrency not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, symbol):
        cryptocurrency = self.get_object(symbol)
        if cryptocurrency:
            serializer = CryptoSerializer(
                cryptocurrency, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Cryptocurrency updated successfully', 'data': serializer.data})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Cryptocurrency not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, symbol):
        cryptocurrency = self.get_object(symbol)
        if cryptocurrency:
            cryptocurrency.delete()
            return Response({'message': 'Cryptocurrency deleted'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'Cryptocurrency not found'}, status=status.HTTP_404_NOT_FOUND)

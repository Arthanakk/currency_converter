from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import os
from rest_framework import status
import requests
from .converter import convert_currency,get_exchange_rates
from .serializers import ConvertSerializer
from .models import Currency_detail
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def covert_currrency(request):
    amount = request.data.get('amount')
    from_currency = request.data.get('from_currency')
    to_currency = request.data.get('to_currency')

    if amount is None or from_currency is None or to_currency is None:
        return Response({'error':'Please provide amount, from_currency, to_currency'},status=status.HTTP_400_BAD_REQUEST)
    try:
        rates = get_exchange_rates()
        if from_currency in rates and to_currency in rates:
            converstion_rate = rates[to_currency] / rates[from_currency]
        else:
            raise ValueError("Currency not found.")
        result = convert_currency(amount,from_currency,to_currency)
        conversion_record = Currency_detail.objects.create(
            amount = amount,
            from_currency = from_currency,
            to_currency = to_currency,
            converted_amount = result,
            converstion_rate = converstion_rate
        )
        print("converstion rate",converstion_rate)
        serializer = ConvertSerializer(conversion_record)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
     return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def live_exchange_rates(request):
    try:
        rates = get_exchange_rates()
        return Response({'rates': rates}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def conversion_history(request):
    try:
        history = Currency_detail.objects.all()  # You can filter by user if needed
        serializer = ConvertSerializer(history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

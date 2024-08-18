from  django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        seriralizer = DrinkSerializer(drinks, many=True)
        return JsonResponse({'drinks':seriralizer.data})
    
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request,id):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        seriralizer = DrinkSerializer(drink)
        return JsonResponse({'drink':seriralizer.data})
    
    if request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
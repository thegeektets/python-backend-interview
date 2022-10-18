from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser

from .models import Trip
from .serializers import TripSerializer
# Create your views here.
from django.http import HttpResponse


@require_http_methods(["GET"])
def index(request):
    trips = Trip.objects.all()
    serialized_data = TripSerializer(trips, many=True)
    return JsonResponse({"status": True, "trips": serialized_data.data}, safe=False, status=200);


@require_http_methods(["POST"])
def store(request):
    payload = JSONParser().parse(request)
    serializer = TripSerializer(data=payload)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=403)

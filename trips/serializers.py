from rest_framework import serializers
from .models import Trip


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ('id', 'driver_id', 'customer_id','vehicle_id',
                  'address', 'address_type', 'cargo_tonnage')
        read_only_fields = ('created_at', 'updated_at')

from django.test import TestCase

# Create your tests here.
from .models import Trip

class TripsTestCase(TestCase):
    def setUp(self):
        Trip.objects.create( 
            driver_id = 21,
            vehicle_id = 200,
            customer_id = 3,
            address = "Kahawa Wendani",
            address_type = "pickup_point",
            cargo_tonnage = 12.20)

    def test_for_id(self):
        trip = Trip.objects.get(vehicle_id=200)
        self.assertEqual(trip.address, 'Kahawa Wendani')



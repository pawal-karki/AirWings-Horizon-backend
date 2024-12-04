from rest_framework import serializers
from .models import Flight,  Schedule , Booking

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    flight_details = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = ['id', 'flight', 'frequency', 'status', 'flight_details']

    def get_flight_details(self, obj):
        return {
            'flight_id': obj.flight.flight_id,
            'airline': obj.flight.airline,
            'departure_city': obj.flight.departure_city,
            'arrival_city': obj.flight.arrival_city
        }


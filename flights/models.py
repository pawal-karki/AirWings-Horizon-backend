from django.db import models
class Flight(models.Model):
    flight_id = models.CharField(max_length=10, unique=True)
    airline = models.CharField(max_length=100)
    departure_airport = models.CharField(max_length=100)
    departure_code = models.CharField(max_length=3)
    departure_city = models.CharField(max_length=100)
    departure_country = models.CharField(max_length=100)
    departure_date = models.DateTimeField()
    arrival_airport = models.CharField(max_length=100)
    arrival_code = models.CharField(max_length=3)
    arrival_city = models.CharField(max_length=100)
    arrival_country = models.CharField(max_length=100)
    arrival_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # e.g., 100.00
    available_seats = models.PositiveIntegerField(default=0)  # e.g., 50 seats
    departure_time = models.TimeField(null=True, blank=True)
    arrival_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.flight_id} - {self.departure_city} to {self.arrival_city}"


class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="bookings")
    passenger_name = models.CharField(max_length=100)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.passenger_name} - {self.flight.flight_id}"

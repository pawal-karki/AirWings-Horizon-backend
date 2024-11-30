from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    @action(detail=False, methods=['post'])
    def add_flights(self, request):
        flights_data = request.data.get('flights', [])
        created_flights = []

        for flight_data in flights_data:
            departure = flight_data.pop('departure', {})
            arrival = flight_data.pop('arrival', {})

            flight_data['departure_airport'] = departure.get('airport')
            flight_data['departure_code'] = departure.get('code')
            flight_data['departure_city'] = departure.get('city')
            flight_data['departure_country'] = departure.get('country')
            flight_data['departure_date'] = departure.get('date')
            flight_data['departure_time'] = departure.get('time')
            

            flight_data['arrival_airport'] = arrival.get('airport')
            flight_data['arrival_code'] = arrival.get('code')
            flight_data['arrival_city'] = arrival.get('city')
            flight_data['arrival_country'] = arrival.get('country')
            flight_data['arrival_date'] = arrival.get('date')
            flight_data['arrival_time'] = arrival.get('time')

            # Add price and available seats
            flight_data['price'] = flight_data.get('price')
            flight_data['available_seats'] = flight_data.get('available_seats', 0)

            serializer = self.get_serializer(data=flight_data)
            if serializer.is_valid():
                serializer.save()
                created_flights.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(created_flights, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def search(self, request):
        departure_city = request.query_params.get('departure_city')
        arrival_city = request.query_params.get('arrival_city')
        max_price = request.query_params.get('max_price')

        queryset = self.get_queryset()

        if departure_city:
            queryset = queryset.filter(departure_city__icontains=departure_city)
        if arrival_city:
            queryset = queryset.filter(arrival_city__icontains=arrival_city)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

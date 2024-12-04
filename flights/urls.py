from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlightViewSet, BookingViewSet , ScheduleViewSet 
router = DefaultRouter()
router.register(r'flights', FlightViewSet, basename='flight')
router.register(r'bookings', BookingViewSet )
router.register(r'schedule', ScheduleViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
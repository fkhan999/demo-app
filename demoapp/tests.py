from django.test import TestCase

# Create your tests here.
from demoapp.models import Booking,BookingSlot


booking_slots = BookingSlot.objects.filter(enabled=True).order_by('booking_date')
print(booking_slots)
# from datetime import date

# Booking.objects.create(
#     booking_date=date(2025, 11, 25),

#     cubicle_code="NOSTP 02 16 A 058",
#     location="Noida, NOIDA-STP, BHUT01, FLOOR-16, A Wing"
# )
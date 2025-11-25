from django.shortcuts import render
from demoapp.models import Booking
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    bookings = Booking.objects.filter(enabled=True).order_by('booking_date')
    print(bookings)
    return render(request, 'index.html', {'bookings': bookings})

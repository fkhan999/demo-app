from django.shortcuts import render
from demoapp.models import Booking,BookingSlot
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'index.html')


@login_required
def slot(request):
    booking_slots = BookingSlot.objects.filter(enabled=True)
    return render(request, 'slot.html', {'booking_slots': booking_slots})

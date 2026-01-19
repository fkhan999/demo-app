from django.shortcuts import render,redirect
from datetime import date
from demoapp.models import Booking,BookingSlot
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'index.html')


@login_required
def slot(request):
    booking_slots = BookingSlot.objects.filter(enabled=True).order_by('booking_date')
    return render(request, 'slot.html', {'booking_slots': booking_slots})


@login_required
def generate_booking(request):
    today = date.today()
    
    # Check if a slot exists for today
    if not BookingSlot.objects.filter(booking_date=today).exists():
        # Find the most recent previous slot
        last_slot = BookingSlot.objects.filter(booking_date__lt=today).order_by('-booking_date').first()
        if last_slot:
            # Update it to today and ensure enabled
            last_slot.booking_date = today
            last_slot.enabled = True
            last_slot.save()
            
    # Disable all past slots
    BookingSlot.objects.filter(booking_date__lt=today).update(enabled=False)
    
    # Show active slots
    booking_slots = BookingSlot.objects.filter(enabled=True).order_by('booking_date')
    return redirect('slot')

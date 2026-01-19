from django.db import models

class Booking(models.Model):

    booking_date = models.DateField()
    cubicle_code = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    enabled = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.booking_date} {self.cubicle_code} - {self.location}"

class BookingSlot(models.Model):
    booking_date = models.DateField()
    cubicle_code = models.CharField(max_length=100, default="NOSTP 02 16 A 001")
    location = models.CharField(max_length=255, default="Noida, NOSTP, BHUT01, FLOOR-16, A")
    slot_start = models.CharField(default="08:00AM", max_length=10)
    slot_end = models.CharField(default="02:00PM", max_length=10)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.booking_date} {self.cubicle_code} {self.location} {self.slot_start} - {self.slot_end}"

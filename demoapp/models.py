from django.db import models

class Booking(models.Model):

    booking_date = models.DateField()
    cubicle_code = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    enabled = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.booking_date} {self.cubicle_code} - {self.location}"

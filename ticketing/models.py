import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Shuttle(models.Model):
    """Model representing an Shuttle."""
    shuttle_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                     help_text='Unique ID for this particular shuttle')
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    color = models.CharField(max_length=100)
    operated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['capacity', 'color']

    def get_absolute_url(self):
        """Returns the URL to access a particular shuttle instance."""
        return reverse('shuttle_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'


class ShuttleSchedule(models.Model):
    """Model representing an Shuttle_schedule."""
    shuttle_sched_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                     help_text='Unique ID for this particular shuttle schedule')
    schd_time = models.TimeField()
    schd_date = models.DateField()
    shuttle_id = models.ForeignKey('Shuttle', on_delete=models.RESTRICT, null=True)

    class Meta:
        ordering = ['schd_date', 'schd_time']

    def get_absolute_url(self):
        """Returns the URL to access a particular shuttle scheudle instance."""
        return reverse('ShuttleSchedule', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.shuttle_sched_id}'


class Ticket(models.Model):
    """Model representing an Shuttle_schedule."""
    # // customer_id, purchased_date, payment_status, shuttle_schd_id
    ticket_number = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                     help_text='Unique ID for this particular ticket purchased')
    purchased_date = models.DateField()
    shuttle_schd_id = models.ForeignKey('ShuttleSchedule', on_delete=models.RESTRICT, null=True)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    class Meta:
        ordering = ['purchased_date']

    def get_absolute_url(self):
        """Returns the URL to access a particular shuttle schedule instance."""
        return reverse('Ticket', args=[str(self.ticket_number)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.ticket_number}'

#    def is_past(self):
#        """Boolean to determine if ticket is in the past"""
#        return bool(self.shuttle_schd_id.schd_date and date.today() < self.shuttle_schd_id.schd_date)

##    def is_today(self):
#        """Boolean to determine if ticket is today"""
##        return bool(self.schd_date == date.today)

##    def refundable(self):
#        """Boolean to determine if ticket is still refundable (more than 24 hours in advance)"""
## THIS IS WRONG CALC - NEEDS TO DETERMINE IF MORE THAN 1 DAY
##        return bool(self.schd_date and date.today < self.schd_date)


class PaymentDetails(models.Model):
    """Model representing an PaymentStatus."""

# look for loan status 
    PAID = 'PAID'
    CANCELLED = 'CANCELLED'
    PENDING = 'PENDING'
    NO_STATUS = 'NO_STATUS'
    PAYMENT_STATUS_OPTIONS = (
        (PAID, 'Paid'),
        (CANCELLED, 'Cancelled'),
        (PENDING, 'Pending'),
        (NO_STATUS, 'No_status'),
    )
    payment_status = models.CharField(
        max_length=50,
        choices=PAYMENT_STATUS_OPTIONS,
        default=NO_STATUS,
    )

    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                      help_text='Unique ID for this particular transaction')
    payment_method = models.CharField(max_length=100)
    amount = models.IntegerField()
    ticket = models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['payment_status', 'payment_method', 'amount']

    def get_absolute_url(self):
        """Returns the URL to access a particular shuttle instance."""
        return reverse('shuttle_detail', args=[str(self.transaction_id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.transaction_id}'

import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date, datetime, timedelta


class Shuttle(models.Model):
    """Model representing an Shuttle."""
    shuttle_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                  help_text='Unique ID for this particular shuttle')
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    color = models.CharField(max_length=100)
    operated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    shuttle_image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        ordering = ['capacity', 'color']

    def get_absolute_url(self):
        """Returns the URL to access a particular shuttle instance."""
        return reverse('shuttle_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'


class ShuttleSchedule(models.Model):
    """Model representing a Shuttle_schedule."""
    shuttle_schd_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
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
        return f'{self.shuttle_schd_id}'


class Ticket(models.Model):
    """Model representing a Shuttle schedule."""
    ticket_number = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                     help_text='Unique ID for this particular ticket purchased')
    purchased_date = models.DateField()
    shuttle_schd_id = models.ForeignKey('ShuttleSchedule', on_delete=models.RESTRICT, null=True)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['purchased_date']

    def get_absolute_url(self):
        """Returns the URL to access a particular ticket instance."""
        return reverse('ticket_detail', args=[str(self.ticket_number)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.ticket_number}'

    def is_past(self):
        """Determines if ticket date is before today."""
        return self.shuttle_schd_id.schd_date < date.today()

    def is_today(self):
        """Determines if ticket date is today."""
        return self.shuttle_schd_id.schd_date == date.today()

    def refundable(self):
        """Determines if ticket is still refundable (more than 24 hours in advance)."""
        return datetime.combine(self.shuttle_schd_id.schd_date, self.shuttle_schd_id.schd_time) - datetime.now() > timedelta(days=1)
        """Boolean to determine if ticket is still refundable (more than 24 hours in advance)"""
        # THIS IS WRONG CALC - NEEDS TO DETERMINE IF MORE THAN 1 DAY
        # return bool(self.shuttle_schd_id.schd_date and date.today() < self.shuttle_schd_id.schd_date)

class PaymentDetails(models.Model):
    """Model representing Payment Details."""
    # look for loan status
    PAID = 'PAID'
    CANCELLED = 'CANCELLED'
    PENDING = 'PENDING'
    NO_STATUS = 'NO_STATUS'
    PAYMENT_STATUS_OPTIONS = (
        (PAID, 'Paid'),
        (CANCELLED, 'Cancelled'),
        (PENDING, 'Pending'),
        (NO_STATUS, 'No Status'),
    )

    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                      help_text='Unique ID for this particular transaction')
    payment_date = models.DateField(null=True, blank=True)  # Added payment date
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_OPTIONS, default=NO_STATUS)
    payment_method = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Changed to DecimalField for monetary values
    ticket = models.ForeignKey('Ticket', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['payment_date', 'payment_status', 'amount']

    def __str__(self):
        return f'Transaction ID: {self.transaction_id}'
        """String for representing the Model object."""
   #     return f'{self.transaction_id}'


class Profile(models.Model):
    profile_id = models.OneToOneField(User, on_delete=models.CASCADE)
#    profile_first = models.OneToOneField(User.first_name, on_delete=models.CASCADE)
#    profile_last = models.OneToOneField(User.last_name, on_delete=models.CASCADE)
#    profile_email = models.OneToOneField(User.email, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default_user.jpg', upload_to='profile_pics')

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.profile_id.username}s Profile'


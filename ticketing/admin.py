from django.contrib import admin
from .models import Shuttle, Ticket, ShuttleSchedule, PaymentDetails
# Register your models here.

admin.site.register(Shuttle)
admin.site.register(Ticket)
admin.site.register(ShuttleSchedule)
admin.site.register(PaymentDetails)


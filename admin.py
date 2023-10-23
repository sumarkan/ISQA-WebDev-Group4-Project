from django.contrib import admin
from .models import Shuttle, ShuttleSchedule, Ticket, PaymentDetails


admin.site.register(Shuttle)
admin.site.register(ShuttleSchedule)
admin.site.register(Ticket)
admin.site.register(PaymentDetails)


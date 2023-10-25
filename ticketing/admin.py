from django.contrib import admin
from .models import Shuttle, Ticket, ShuttleSchedule, PaymentDetails
# Register your models here.

admin.site.register(Shuttle)
admin.site.register(ShuttleSchedule)
admin.site.register(PaymentDetails)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'purchased_date', 'customer', 'shuttle_schd_id')
    list_filter = ('customer', 'purchased_date')

    fieldsets = (
        (None, {
            'fields': ('ticket_number', 'purchased_date')
        }),
        ('Shuttle details', {
            'fields': ('customer', 'shuttle_schd_id')
        }),
    )


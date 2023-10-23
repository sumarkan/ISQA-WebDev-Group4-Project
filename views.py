from django.shortcuts import render
from .models import Shuttle, ShuttleSchedule, Ticket, PaymentDetails


def index(request):
    return render(request, 'index.html')


def shuttle_list(request):
    shuttles = Shuttle.objects.all()
    return render(request, 'shuttle_list.html', {'shuttles': shuttles})


def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'ticket_list.html', {'tickets': tickets})


def schedule_list(request):
    schedules = ShuttleSchedule.objects.all()
    return render(request, 'schedule_list.html', {'schedules': schedules})


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def terms_of_service(request):
    return render(request, 'terms_of_service.html')


def contact_us(request):
    return render(request, 'contact_us.html')


def payment_details_list(request):
    payments = PaymentDetails.objects.all()
    context = {'payments': payments}
    return render(request, 'payment_details_list.html', context)

from django.shortcuts import render
from .models import Shuttle, ShuttleSchedule, Ticket, PaymentDetails
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


def index(request):
    return render(request, 'ticketing/index.html')


def shuttle_list(request):
    shuttle_list = Shuttle.objects.all()
    return render(request, 'shuttle_list.html', {'shuttle_list': shuttle_list})


def ticket_list(request):
    ticket_list = Ticket.objects.all()
    return render(request, 'ticket_list.html', {'ticket_list': ticket_list})


def schedule_list(request):
    schedule_list = ShuttleSchedule.objects.all()
    return render(request, 'schedule_list.html', {'schedule_list': schedule_list})


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


class ShuttleListView(generic.ListView):
    model = Shuttle


class mytickets(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing tickets purchased by the customer logged in"""
    model = Ticket
    template_name = 'my_tickets.html'
    paginate_by = 10

    def get_queryset(self):
        return Ticket.objects.filter \
            (customer=self.request.user).order_by('purchased_date')

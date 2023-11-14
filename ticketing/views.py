from django.shortcuts import render
from .models import Shuttle, ShuttleSchedule, Ticket, PaymentDetails
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.core.mail import send_mail
from django.contrib.auth.models import User

def index(request):
    return render(request, 'ticketing/index.html')

                        # I feel like there should be views - but there aren't for login/logout functions
            # I have no idea where the view is coming from
        # in urls.py it says auth_views unlike others
            # am I missing a library or a view??

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


class MyTickets(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing tickets purchased by the customer logged in"""
    model = Ticket
    template_name = 'my_tickets.html'
    paginate_by = 10

    def get_queryset(self):
        return Ticket.objects.filter\
            (customer=self.request.user).order_by('purchased_date')


class MyAccount(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing tickets purchased by the customer logged in"""
    model = Ticket
    template_name = 'my_account.html'
    paginate_by = 10

    def get_queryset(self):
        return Ticket.objects.filter\
            (customer=self.request.user).order_by('purchased_date')

class PasswordResetView(generic.ListView):
    """Generic class-based view listing tickets purchased by the customer logged in"""
    model = Ticket #UNSURE ABOUT THIS ************
    template_name = 'registration/password_reset_form.html'
    paginate_by = 10

    def get_queryset(self):
        return Ticket.objects.filter\
            (customer=self.request.user).order_by('purchased_date')

class PasswordResetDoneView(generic.ListView):
    """Generic class-based view listing tickets purchased by the customer logged in"""
    model = Ticket #UNSURE ABOUT THIS ************
    template_name = 'registration/password_reset_done.html'
    paginate_by = 10

    def get_queryset(self):
        return Ticket.objects.filter\
            (customer=self.request.user).order_by('purchased_date')

class PasswordResetConfirmView(generic.ListView):
    """Generic class-based view listing tickets purchased by the customer logged in"""
    model = Ticket #UNSURE ABOUT THIS ************
    template_name = 'registration/password_reset_confirm.html'
    paginate_by = 10

    def get_queryset(self):
        return Ticket.objects.filter\
            (customer=self.request.user).order_by('purchased_date')

class PasswordResetCompleteView(generic.ListView):
    """Generic class-based view listing tickets purchased by the customer logged in"""
    model = Ticket #UNSURE ABOUT THIS ************
    template_name = 'registration/password_reset_complete.html'
    paginate_by = 10

    def get_queryset(self):
        return Ticket.objects.filter\
            (customer=self.request.user).order_by('purchased_date')

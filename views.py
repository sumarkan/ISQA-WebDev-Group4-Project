from .models import Shuttle, ShuttleSchedule, Ticket, PaymentDetails
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth.models import User


def home(request):
    context = {'show_back_button': False}
    return render(request, 'ticketing/base.html', context)


# Index view
def index(request):
    context = {'show_back_button': False}
    return render(request, 'ticketing/index.html', context)


# Shuttle list view
def shuttle_list(request):
    list_shuttles = Shuttle.objects.all()
    context = {
        'shuttle_list': list_shuttles,
        'show_back_button': True
    }
    return render(request, 'shuttle_list.html', context)


class ShuttleCreate(CreateView):
    model = Shuttle
    fields = ['name', 'capacity', 'color', 'operated_by']
    template_name = 'shuttle_create.html'


class ShuttleUpdate(UpdateView):
    model = Shuttle
    fields = ['name', 'capacity', 'color', 'operated_by']
    template_name = 'shuttle_update.html'  #

    def get_success_url(self):
        """
        After successfully updating the shuttle, redirect to the shuttle list.
        """
        return reverse_lazy('shuttle_list')

class ShuttleDelete(DeleteView):
    model = Shuttle
    template_name = 'shuttle_confirm_delete.html'  # Specify your template name here
    success_url = reverse_lazy('shuttle_list')  # Redirect to shuttle list after deleting

    def get_context_data(self, **kwargs):
        """
        Provide additional context to the template, if needed.
        """
        context = super(ShuttleDelete, self).get_context_data(**kwargs)
        return context


# Ticket list view
def ticket_list(request):
    list_tickets = Ticket.objects.all()
    context = {
        'ticket_list': list_tickets,
        'show_back_button': True
    }
    return render(request, 'ticket_list.html', context)


# Schedule list view
def schedule_list(request):
    lists_schd_shuttles = ShuttleSchedule.objects.all()
    context = {
        'schedule_list': lists_schd_shuttles,
        'show_back_button': True
    }
    return render(request, 'schedule_list.html', context)

def my_ticket_number(request):
    return render(request, 'my_ticket_number.html', context = {'show_back_button': True})

def payment_details_list(request):
    if request.method == 'POST':
        ticket_number = request.POST.get('ticket_number')
        try:
            ticket = Ticket.objects.get(ticket_number=ticket_number)
            payment_details = PaymentDetails.objects.filter(ticket=ticket)
            return render(request, 'payment_details_list.html', {'payment_details_list': payment_details, 'show_back_button': True})
        except Ticket.DoesNotExist:
            # Handle the case where the ticket does not exist
            return render(request, 'my_ticket_number.html', {'error': 'Ticket not found'})
    else:
        return redirect('my_ticket_number')


# Payment details list view
def payment_details_list(request):
    payments = PaymentDetails.objects.all()
    context = {
        'payments': payments,
        'show_back_button': True
    }
    return render(request, 'payment_details_list.html', context)
def payment_detail_view(request, payment_id):
    payment = get_object_or_404(payment_details_list, pk=payment_id, user=request.user)
    return render(request, 'payment_detail.html', {'payment': payment,  'show_back_button': True})


# Privacy policy view
def privacy_policy(request):
    context = {'show_back_button': True}
    return render(request, 'privacy_policy.html', context)


# Terms of service view
def terms_of_service(request):
    context = {'show_back_button': True}
    return render(request, 'terms_of_service.html', context)


# Contact us view
def contact_us(request):
    context = {'show_back_button': True}
    return render(request, 'contact_us.html', context)


class ShuttleCreate(CreateView):
    model = Shuttle
    fields = ['name', 'capacity', 'color', 'operated_by']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('shuttle_list'))


class ShuttleUpdate(UpdateView):
    model = Shuttle
    fields = ['name', 'capacity', 'color', 'operated_by']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('shuttle_list'))


def shuttle_delete(request, pk):
    shuttle = get_object_or_404(Shuttle, pk=pk)
    try:
        shuttle.delete()
        messages.success(request, (shuttle.name + " has been deleted"))
    except:
        messages.success(request, (shuttle.name + ' cannot be deleted, Shuttle does not exists'))

    return redirect('shuttle_list')
        # return Ticket.objects.filter(customer=self.request.user).order_by('purchased_date')


class MyAccount(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing tickets purchased by the customer logged in"""
    model = Ticket
    template_name = 'my_account.html'
    paginate_by = 10

    def get_queryset(self):
        return Ticket.objects.filter\
            (customer=self.request.user).order_by('purchased_date')


class MyTickets(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing tickets purchased by the customer logged in"""
    model = Ticket
    template_name = 'my_tickets.html'
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


class ShuttleScheduleCreate(CreateView):
    model = ShuttleSchedule
    fields = ['schd_time', 'schd_date', 'shuttle_id']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('schedule_list'))


class ShuttleScheduleUpdate(UpdateView):
    model = ShuttleSchedule
    fields = ['schd_time', 'schd_date', 'shuttle_id']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('schedule_list'))


def shuttleschedule_delete(request, pk):
    schedule = get_object_or_404(ShuttleSchedule, pk=pk)
    name = schedule.shuttle_id.name
    try:
        schedule.delete()
        messages.success(request, ('schedule for shuttle with '+name + " has been deleted"))
    except:
        messages.success(request, ('schedule for shuttle with '+name + ' cannot be deleted, Shuttle does not exists'))

    return redirect('schedule_list')
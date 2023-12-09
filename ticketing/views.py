from .models import Shuttle, ShuttleSchedule, Ticket, PaymentDetails, Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User


def index(request):
    return render(request, 'ticketing/index.html')


def home(request):
    return render(request, 'ticketing/base.html')


# class for Shuttle Lists
class ShuttleListView(generic.ListView):
    model = Shuttle


def shuttle_list(request):
    list_shuttles = Shuttle.objects.all()
    return render(request, 'shuttle_list.html', {'shuttle_list': list_shuttles})


# class for ticket lists
class TicketListView(generic.ListView):
    model = Ticket


def ticket_list(request):
    list_tickets = Ticket.objects.all()
    return render(request, 'ticket_list.html', {'ticket_list': list_tickets})


# class TicketDetailView(generic.DetailView)
#    model = Ticket


class ScheduleListView(generic.ListView):
    model = ShuttleSchedule


def schedule_list(request):
    lists_schd_shuttles = ShuttleSchedule.objects.all()
    return render(request, 'schedule_list.html', {'schedule_list': lists_schd_shuttles})


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


class MyAccount(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing tickets purchased by the customer logged in"""
    model = Profile
    template_name = 'my_account.html'
    paginate_by = 10

    def get_queryset(self):
        return Profile.objects.filter \
            (customer=self.request.user).order_by('purchased_date')


# do i really need this? - i don't understand - Jill
def profile_list(request):
    list_profiles = Profile.objects.all()
    return render(request, 'profile_list.html', {'profile_list': list_profiles})


class ProfileDetail(generic.DetailView):
    model = Profile


def profile_detail(request):
    detailed_profile = Profile.objects.all()
    return render(request, 'profile_list.html', {'profile_list': detailed_profile})


class ProfileCreate(CreateView):
    model = Profile
    fields = ['profile_id', 'profile_first', 'profile_last', 'profile_email', 'profile_image']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('myaccount'))


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['profile_id', 'profile_first', 'profile_last', 'profile_email', 'profile_image']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('myaccount'))


class MyTickets(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing tickets purchased by the customer logged in"""
    model = Ticket
    template_name = 'my_tickets.html'
    paginate_by = 10

    def get_queryset(self):
        return Ticket.objects.filter \
            (customer=self.request.user).order_by('purchased_date')


class PasswordResetView(generic.ListView):
    """Generic class-based view listing tickets purchased by the customer logged in"""
    model = Ticket  # UNSURE ABOUT THIS ************
    template_name = 'registration/password_reset_form.html'
    paginate_by = 10

    def get_queryset(self):
        return Ticket.objects.filter \
            (customer=self.request.user).order_by('purchased_date')


class PasswordResetDoneView(generic.ListView):
    """Generic class-based view listing tickets purchased by the customer logged in"""
    model = Ticket  # UNSURE ABOUT THIS ************
    template_name = 'registration/password_reset_done.html'
    paginate_by = 10

    def get_queryset(self):
        return Ticket.objects.filter \
            (customer=self.request.user).order_by('purchased_date')


class PasswordResetConfirmView(generic.ListView):
    """Generic class-based view listing tickets purchased by the customer logged in"""
    model = Ticket  # UNSURE ABOUT THIS ************
    template_name = 'registration/password_reset_confirm.html'
    paginate_by = 10

    def get_queryset(self):
        return Ticket.objects.filter \
            (customer=self.request.user).order_by('purchased_date')


class PasswordResetCompleteView(generic.ListView):
    """Generic class-based view listing tickets purchased by the customer logged in"""
    model = Ticket  # UNSURE ABOUT THIS ************
    template_name = 'registration/password_reset_complete.html'
    paginate_by = 10

    def get_queryset(self):
        return Ticket.objects.filter \
            (customer=self.request.user).order_by('purchased_date')

from django.urls import path
from . import views
from .views import ShuttleCreate, ShuttleUpdate, ShuttleDelete

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('shuttle_list/', views.shuttle_list, name='shuttle_list'),
    path('shuttle/create/', ShuttleCreate.as_view(), name='shuttle_create'),
    path('shuttle/<uuid:pk>/update/', ShuttleUpdate.as_view(), name='shuttle_update'),
    path('shuttle/<uuid:pk>/delete/', ShuttleDelete.as_view(), name='shuttle_delete'),
    path('alltickets/', views.ticket_list, name='ticket_list'),
    path('schedule/', views.schedule_list, name='schedule_list'),
    path('my_ticket_number/', views.my_ticket_number, name='my_ticket_number'),
    path('payment_details_list/', views.payment_details_list, name='payment_details'),
    path('payments/', views.payment_details_list, name='payment_details_list'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('shuttle/create/', views.ShuttleScheduleCreate.as_view(), name='shuttleschedule_create'),
    path('shuttle/<uuid:pk>/update/', views.ShuttleScheduleUpdate.as_view(), name='shuttleschedule_update'),
    path('shuttle/<uuid:pk>/delete/', views.shuttleschedule_delete, name='shuttleschedule_delete'),
    path('mytickets/', views.MyTickets.as_view(), name='mytickets'),
    path('myaccount/', views.MyAccount.as_view(), name='myaccount'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'), # COPIED FROM TUTORIAL
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile_detail/<int:pk>', views.ProfileDetail.as_view(), name='profile_detail'),
    path('schedule/create/', views.ShuttleScheduleCreate.as_view(), name='shuttleschedule_create'),
    path('schedule/<uuid:pk>/update/', views.ShuttleScheduleUpdate.as_view(), name='shuttleschedule_update'),
    path('schedule/<uuid:pk>/delete/', views.shuttleschedule_delete, name='shuttleschedule_delete'),
    path('ticket/create/', views.TicketCreate.as_view(), name='ticket_create'),
    path('ticket/<uuid:pk>/update/', views.TicketUpdate.as_view(), name='ticket_update'),
    path('ticket/<uuid:pk>/delete/', views.ticket_delete, name='ticket_delete'),
]

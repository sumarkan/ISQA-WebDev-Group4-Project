from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shuttles/', views.shuttle_list, name='shuttle_list'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('schedule/', views.schedule_list, name='schedule_list'),
    path('payments/', views.payment_details_list, name='payment_details_list'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('mytickets/', views.MyTickets.as_view(), name='mytickets'),
    path('myaccount/', views.MyAccount.as_view(), name='myaccount'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
   # path('accounts/', include('django.contrib.auth.urls')), # COPIED FROM TUTORIAL
]
    # IMPORTANT – THE URL BELOW MUST BE AFTER THE PASSWORD RESET CUSTOM FORM ABOVE if included- was in front of the reset password
            # bringing up the django version first
 # path('', include('django.contrib.auth.urls')),

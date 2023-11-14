from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shuttle_list/', views.shuttle_list, name='shuttle_list'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('schedule/', views.schedule_list, name='schedule_list'),
    path('payments/', views.payment_details_list, name='payment_details_list'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('mytickets/', views.mytickets.as_view(), name='mytickets'),
    path('shuttle/create/', views.ShuttleCreate.as_view(), name='shuttle_create'),
    path('shuttle/<int:pk>/update/', views.ShuttleUpdate.as_view(), name='shuttle_update'),
    path('shuttle/<int:pk>/delete/', views.shuttle_delete, name='shuttle_delete'),
]
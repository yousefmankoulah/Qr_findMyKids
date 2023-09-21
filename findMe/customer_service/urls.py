from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactus, name='contactus'),
    path('opendTickets/', views.opendTickets, name='opendTickets'),
    path('allTickets', views.allTickets, name='allTickets'),
    path('ticketDetails/<int:id>', views.updateTickets, name='updateTickets'),
    path('closedTickets/', views.closedTickets, name="closedTickets"),
    path('createTickets/', views.createTickets, name="createTickets"),
    path('filterTickets/', views.filterTickets, name="filterTickets"),
]
    
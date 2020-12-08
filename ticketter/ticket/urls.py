from django.urls import path
from . import views

urlpatterns = [
    path(route='create-ticket/', view=views.create_ticket, name='create-ticket'),
    path(route='view-tickets/', view=views.view_tickets, name='view-tickets'),
]
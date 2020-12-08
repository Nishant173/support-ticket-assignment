from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import TicketCreationForm
from .models import Ticket
from .utils import assemble_ticket_dictionary
from api.crud_ops import get_tickets, post_ticket
from api.filters import filter_tickets


# @login_required
# def create_ticket(request):
#     if request.method == 'POST':
#         form = TicketCreationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request=request, message="Ticket has been created")
#             return redirect(to='account-home')
#     else:
#         form = TicketCreationForm(initial={'username': request.user.username})
#     return render(request=request, template_name='ticket/create_ticket.html', context={'form': form})


# @login_required
# def view_tickets(request):
#     tickets = Ticket.objects.filter(username__exact=request.user.username)
#     is_empty = (len(tickets) == 0)
#     context = {
#         'tickets': tickets,
#         'is_empty': is_empty,
#     }
#     return render(request=request, template_name='ticket/view_tickets.html', context=context)


@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketCreationForm(data=request.POST)
        if form.is_valid():
            dict_obj = form.cleaned_data
            dict_obj = assemble_ticket_dictionary(dict_obj=dict_obj, request_obj=request)
            response = post_ticket(dict_obj=dict_obj)
            if response.get('status_code', '') in [200, 201]:
                messages.success(request=request, message="Ticket has been created")
                return redirect(to='account-home')
    else:
        form = TicketCreationForm(initial={'username': request.user.username})
    return render(request=request, template_name='ticket/create_ticket.html', context={'form': form})


@login_required
def view_tickets(request):
    tickets = get_tickets()
    tickets = filter_tickets(tickets=tickets, email=request.user.email)
    is_empty = (len(tickets) == 0)
    context = {
        'tickets': tickets,
        'is_empty': is_empty,
    }
    return render(request=request, template_name='ticket/view_tickets.html', context=context)
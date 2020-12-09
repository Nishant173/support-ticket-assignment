from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import TicketCreationForm
from .models import Ticket
from . import utils
from api import (crud_ops as api_crud_ops,
                 errors as api_errors,
                 filters as api_filters)


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
            dict_obj = utils.map_model2api(dict_obj=dict_obj, email=request.user.email)
            response = api_crud_ops.post_ticket(dict_obj=dict_obj)
            if response.get('status_code', '') in [200, 201]:
                messages.success(request=request, message="Ticket has been created")
                return redirect(to='account-home')
            else:
                status_code = response.get('status_code', 'Backend')
                messages.warning(request=request,
                                 message=f"{status_code} error. Please try again later")
    else:
        form = TicketCreationForm(initial={'username': request.user.username})
    return render(request=request, template_name='ticket/create_ticket.html', context={'form': form})


@login_required
def view_tickets(request):
    username = request.user.username
    try:
        tickets = api_crud_ops.get_tickets()
    except api_errors.BadApiRequestError:
        context = {'tickets': [], 'is_empty': True, 'is_error': True, 'username': username}
    else:
        tickets = api_filters.filter_tickets(tickets=tickets, email=request.user.email)
        is_empty = (len(tickets) == 0)
        context = {
            'tickets': tickets,
            'is_empty': is_empty,
            'is_error': False,
            'username': username,
        }
    return render(request=request, template_name='ticket/view_tickets.html', context=context)
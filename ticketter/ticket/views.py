from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import TicketCreationForm
from .models import Ticket


@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request=request, message="Ticket has been created")
            return redirect(to='account-home')
    else:
        form = TicketCreationForm(initial={'username': request.user.username})
    return render(request=request, template_name='ticket/create_ticket.html', context={'form': form})


@login_required
def view_tickets(request):
    tickets = Ticket.objects.all() # username__exact=request.username
    is_empty = (len(tickets) == 0)
    context = {
        'tickets': tickets,
        'is_empty': is_empty,
    }
    return render(request=request, template_name='ticket/view_tickets.html', context=context)
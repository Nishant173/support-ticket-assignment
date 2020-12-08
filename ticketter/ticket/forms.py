from django import forms
from .models import Ticket


class TicketCreationForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        # fields = ('department', 'category', 'project_url', 'subject', 'description', 'priority')
from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'date_joined', 'is_active',
                    'is_admin', 'is_staff', 'is_superuser')
    list_filter = ('is_admin', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')


admin.site.register(Account, AccountAdmin)
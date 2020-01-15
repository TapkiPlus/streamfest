from django.contrib import admin
from .models import *

admin.site.register(Speaker)
admin.site.register(Ticket)

class OrderAdmin(admin.ModelAdmin):
    search_fields = ('customerFio', 'customerPhone', 'customerEmail',)
    list_filter = ('isPayed', 'ticket', 'isCheckIn', 'isSpecial',)
    class Meta:
        model = Order
admin.site.register(Order, OrderAdmin)
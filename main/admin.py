from django.contrib import admin
from rangefilter.filter import DateRangeFilter
from django.contrib.auth.models import Group, User

from .models import Order, Agent


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created', 'price', 'agent', 'description')
    list_filter = (('created', DateRangeFilter),)
    empty_value_display = '-пусто-'
    list_per_page = 10

class AgentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    list_per_page = 10

admin.site.site_header = 'Order Manager'
admin.site.register(Order, OrderAdmin)
admin.site.register(Agent, AgentAdmin)
# admin.site.unregister(Group)
# admin.site.unregister(User)
admin.site.header = 'My project'
admin.site.title = 'HTML title from adminsitration'
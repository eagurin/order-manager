from django.contrib import admin
from rangefilter.filter import DateRangeFilter
from django.contrib.auth.models import Group, User

from .models import Order, Agent

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'price', 'agent', 'short_description')
    list_filter = (('created', DateRangeFilter),)
    empty_value_display = '-пусто-'
    list_per_page = 10

class AgentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    list_per_page = 10


admin.site.register(Order, OrderAdmin)
admin.site.register(Agent, AgentAdmin)
from djmoney.models.fields import MoneyField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Agent(models.Model):
    name = models.CharField(_('name'), max_length=28)


    class Meta:
        verbose_name = "counter-agent"

    def __str__(self):
        return self.name


class Order(models.Model):
    created = models.DateTimeField(
        _('data create'), auto_now_add=True, db_index=True)
    price = MoneyField(_('price'), max_digits=14,
                       decimal_places=0, default_currency='RUB')
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name="orders")
    description = models.TextField(_('description'),)

    class Meta:
        verbose_name = "order"
        ordering = ('id',)

    def __str__(self):
        return '№ ' + str(self.id)
        
    # def __str__(self):
    #     return self.id

from django.db import models
from django.template.defaultfilters import truncatechars
from djmoney.models.fields import MoneyField


class Agent(models.Model):
    name = models.CharField(max_length=28)

    class Meta:
        verbose_name = "counter-agent"

    def __str__(self):
        return self.name


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    price = MoneyField(max_digits=14, decimal_places=0, default_currency='RUB')
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name="orders")
    description = models.TextField(max_length=480)

    class Meta:
        verbose_name = "order"
        ordering = ('id',)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    def __str__(self):
        return '№ ' + str(self.id)


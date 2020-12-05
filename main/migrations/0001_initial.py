# Generated by Django 3.1.3 on 2020-11-27 04:07

import django.db.models.deletion
import djmoney.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=28)),
            ],
            options={
                'verbose_name': 'contractor',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('price_currency', djmoney.models.fields.CurrencyField(choices=[('EUR', 'Euro'), ('RUB', 'Russian Ruble'), ('USD', 'US Dollar')], default='RUB', editable=False, max_length=3)),
                ('price', djmoney.models.fields.MoneyField(decimal_places=0, default_currency='RUB', max_digits=14)),
                ('description', models.TextField(max_length=320)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='main.agent')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]

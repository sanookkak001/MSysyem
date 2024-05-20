# Generated by Django 4.2.5 on 2024-03-24 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0011_channel_currency_quarter_dividend_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dividend_history',
            name='Ticker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stock.symbol'),
        ),
    ]

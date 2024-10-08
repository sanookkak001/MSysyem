# Generated by Django 4.2.5 on 2024-03-07 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0009_rename_stock_stock_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.FloatField(default=0)),
                ('AvgPrice', models.FloatField(default=0)),
                ('Symbol_Ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stock.symbol', unique=True)),
            ],
        ),
    ]

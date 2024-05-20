# Generated by Django 4.2.5 on 2024-02-16 15:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TypeSector', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='Date',
            new_name='Day',
        ),
        migrations.AddField(
            model_name='stock',
            name='Amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='AvgPrice',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='Bath',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='DateRecord',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='Rate',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='Values',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Symbolname', models.CharField(max_length=255)),
                ('TypeSector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stock.type')),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='Symbol',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Stock.symbol'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='Type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Stock.type'),
            preserve_default=False,
        ),
    ]

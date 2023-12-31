# Generated by Django 4.1.7 on 2023-03-16 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cryptocurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('symbol', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('percent_change_1h', models.DecimalField(decimal_places=2, max_digits=20)),
                ('percent_change_24h', models.DecimalField(decimal_places=2, max_digits=20)),
                ('percent_change_7d', models.DecimalField(decimal_places=2, max_digits=20)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=20)),
                ('market_cap', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-16 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cryptocurrency', '0002_alter_cryptocurrency_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='market_cap',
            field=models.DecimalField(decimal_places=0, max_digits=20, verbose_name='Рыночная капитализация'),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='percent_change_1h',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='1ч %'),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='percent_change_24h',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='24ч %'),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='percent_change_7d',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='7д %'),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Текущий курс'),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='symbol',
            field=models.CharField(max_length=50, verbose_name='Символьный код'),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='volume',
            field=models.DecimalField(decimal_places=0, max_digits=20, verbose_name='Объем торгов'),
        ),
        migrations.CreateModel(
            name='FavoriteCryptocurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cryptocurrency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cryptocurrency.cryptocurrency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'cryptocurrency')},
            },
        ),
    ]
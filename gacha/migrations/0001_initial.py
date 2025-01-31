# Generated by Django 5.1.5 on 2025-01-31 00:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('credits', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rarity', models.IntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='AccountItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acquired', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gacha.account')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gacha.item')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='items',
            field=models.ManyToManyField(through='gacha.AccountItem', to='gacha.item'),
        ),
    ]

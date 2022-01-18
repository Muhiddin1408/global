# Generated by Django 4.0 on 2022-01-17 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'PENDING'), ('delivering', 'DELIVERING'), ('completed', 'COMPLETED'), ('not cancelled', 'NOT CANCELLED')], default='pending', max_length=16),
        ),
    ]
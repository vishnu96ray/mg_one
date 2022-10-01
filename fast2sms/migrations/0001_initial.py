# Generated by Django 4.1.1 on 2022-10-01 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('mobile', models.BigIntegerField()),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('otp', models.CharField(blank=True, max_length=10, null=True)),
                ('count', models.IntegerField(default=0)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
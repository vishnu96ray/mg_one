# Generated by Django 4.1.1 on 2022-10-01 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('itemAttribution', '0001_initial'),
        ('locationHierarchy', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('in_stock', models.BooleanField(default=False)),
                ('price', models.FloatField(default=1)),
                ('solo_price', models.FloatField(default=1)),
                ('group_price', models.FloatField(default=1)),
                ('max_quantity', models.IntegerField(default=1)),
                ('is_active', models.BooleanField()),
                ('is_searchable', models.BooleanField(default=False)),
                ('item_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='itemAttribution.productproduct')),
                ('location_hierarchy_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locationHierarchy.locationhierarchy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

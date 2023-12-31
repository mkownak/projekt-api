# Generated by Django 4.2.8 on 2023-12-11 18:24

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
            name='Fishery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('', 'wybierz kategorie'), ('River', 'Rzeka'), ('Lake', 'Jezioro'), ('Pond', 'Staw'), ('Sea', 'Morze')], max_length=10)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('date_added', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('Pending', 'Oczekujace'), ('Accepted', 'Zaakceptowane'), ('Discarded', 'Odrzucone')], default='Pending', max_length=20)),
                ('user_added', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

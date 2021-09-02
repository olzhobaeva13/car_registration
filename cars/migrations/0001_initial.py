# Generated by Django 3.2.7 on 2021-09-02 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_issue', models.IntegerField()),
                ('legal_number', models.CharField(max_length=50)),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars', to='directory.mark')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to=settings.AUTH_USER_MODEL)),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='handled_cars', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CarDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='cars.car')),
            ],
        ),
    ]
# Generated by Django 2.2.6 on 2020-04-15 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0009_delete_forgot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forgot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sifre', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('modificationDate', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('code', models.UUIDField(default=uuid.UUID('f35c3205-09e7-4506-9197-956af7003d3c'), editable=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-13 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("trip", "0003_alter_usertrip_travel_type"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserTripMatches",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "match_status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Cancelled", "Cancelled"),
                            ("Matched", "Matched"),
                            ("Unmatched", "Unmatched"),
                        ],
                        default="Pending",
                        max_length=10,
                    ),
                ),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receive_matches",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_matches",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "u_trip",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="trip.usertrip"
                    ),
                ),
            ],
        ),
    ]

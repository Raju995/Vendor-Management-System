# Generated by Django 4.2.4 on 2024-05-02 13:42

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vendor_details",
            fields=[
                ("name", models.CharField(max_length=100)),
                ("contact_details", models.TextField()),
                ("address", models.TextField()),
                (
                    "vendor_code",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
            ],
        ),
    ]

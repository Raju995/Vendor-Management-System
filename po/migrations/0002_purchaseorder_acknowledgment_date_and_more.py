# Generated by Django 4.2.4 on 2024-05-04 08:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("po", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="purchaseorder",
            name="acknowledgment_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="purchaseorder",
            name="acknowledgment_status",
            field=models.CharField(
                choices=[("yes", "Yes"), ("no", "No")], default="No", max_length=10
            ),
        ),
        migrations.AddField(
            model_name="purchaseorder",
            name="delivery_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="purchaseorder",
            name="issue_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="purchaseorder",
            name="items",
            field=models.JSONField(default=""),
        ),
        migrations.AddField(
            model_name="purchaseorder",
            name="order_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="purchaseorder",
            name="quality_rating",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="purchaseorder",
            name="quantity",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="purchaseorder",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("completed", "Completed"),
                    ("cancelled", "Cancelled"),
                ],
                default="Pending",
                max_length=50,
            ),
        ),
    ]

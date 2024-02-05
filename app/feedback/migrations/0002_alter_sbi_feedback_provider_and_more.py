# Generated by Django 4.2.9 on 2024-02-05 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0001_initial"),
        ("feedback", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sbi_feedback",
            name="provider",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sbi_feedback_provided",
                to="employees.employee",
            ),
        ),
        migrations.AlterField(
            model_name="sbi_feedback",
            name="receiver",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sbi_feedback_received",
                to="employees.employee",
            ),
        ),
    ]

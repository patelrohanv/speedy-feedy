from django.core.management.base import BaseCommand
from faker import Faker
import random
from employees.models import Employee
from feedback.models import DESC_Feedback


class Command(BaseCommand):
    help = "Create fake DESC feedback data"

    def add_arguments(self, parser):
        parser.add_argument(
            "count", type=int, help="Number of fake DESC feedbacks to create"
        )

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        fake = Faker()

        employees = list(Employee.objects.all())
        if not employees:
            self.stdout.write(
                self.style.WARNING(
                    "No employees found. Please create some employees first."
                )
            )
            return

        for _ in range(count):
            provider = random.choice(employees)
            receiver = random.choice(employees)
            DESC_Feedback.objects.create(
                describe=fake.text(),
                explain=fake.text(),
                specify=fake.text(),
                consequences=fake.text(),
                provider=provider,
                receiver=receiver,
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created {count} fake DESC feedback entries"
            )
        )

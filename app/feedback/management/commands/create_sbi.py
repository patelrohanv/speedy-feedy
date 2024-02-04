from django.core.management.base import BaseCommand
from faker import Faker
import random
from employees.models import Employee
from feedback.models import SBI_Feedback


class Command(BaseCommand):
    help = "Create fake SBI feedback data"

    def add_arguments(self, parser):
        parser.add_argument(
            "count", type=int, help="Number of fake SBI feedbacks to create"
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
            SBI_Feedback.objects.create(
                situation=fake.text(),
                behavior=fake.text(),
                impact=fake.text(),
                provider=provider,
                receiver=receiver,
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created {count} fake SBI feedback entries"
            )
        )

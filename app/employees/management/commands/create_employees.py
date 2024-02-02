from django.core.management.base import BaseCommand
from employees.models import Employee
import random
import faker


class Command(BaseCommand):
    help = "Create random employees"

    def add_arguments(self, parser):
        parser.add_argument(
            "total", type=int, help="Indicates the number of employees to be created"
        )

    def handle(self, *args, **kwargs):
        total = kwargs["total"]
        fake = faker.Faker()
        for i in range(total):
            Employee.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                phone_number=fake.phone_number(),
                date_of_birth=fake.date_of_birth(minimum_age=30, maximum_age=60),
                date_hired=fake.past_date(start_date="-30y"),
                position=fake.job(),
                department=fake.bs(),
                is_active=random.choice([True, False]),
            )
        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {total} Employee(s)")
        )

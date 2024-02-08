from django.db import models
from employees.models import Employee

class Feedback(models.Model):
    provider = models.ForeignKey(
        Employee, 
         related_name="%(class)s_provided_feedback"
         ,on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        Employee, 
        related_name="%(class)s_received_feedback",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"Feedback from {self.provider} to {self.receiver}"


class SBI_Feedback(Feedback):
    situation = models.TextField()
    behavior = models.TextField()
    impact = models.TextField()


class DESC_Feedback(Feedback):
    describe = models.TextField()
    explain = models.TextField()
    specify = models.TextField()
    consequences = models.TextField()


class GROW_Feedback(Feedback):
    goal = models.TextField()
    reality = models.TextField()
    options = models.TextField()
    will = models.TextField()
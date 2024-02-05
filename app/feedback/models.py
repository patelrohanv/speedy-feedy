from django.db import models
from employees.models import Employee


class SBI_Feedback(models.Model):
    situation = models.TextField()
    behavior = models.TextField()
    impact = models.TextField()
    provider = models.ForeignKey(
        Employee, related_name="sbi_feedback_provided", on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        Employee, related_name="sbi_feedback_received", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"SBI Feedback from {self.provider} to {self.receiver}"


class DESC_Feedback(models.Model):
    describe = models.TextField()
    explain = models.TextField()
    specify = models.TextField()
    consequences = models.TextField()
    provider = models.ForeignKey(
        Employee, related_name="desc_provided_feedback", on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        Employee, related_name="desc_received_feedback", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"DESC Feedback from {self.provider} to {self.receiver}"


# class GROW_Feedback(models.Model):
#     goal = models.TextField()
#     reality = models.TextField()
#     options = models.TextField()
#     will = models.TextField()
# provider = models.ForeignKey(
#     Employee, related_name='grow_provided_feedback', on_delete=models.CASCADE
# )
# receiver = models.ForeignKey(
#     Employee, related_name='grow_received_feedback', on_delete=models.CASCADE
# )
# created_at = models.DateTimeField(auto_now_add=True)
# updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"GROW Feedback from {self.provider} to {self.receiver}"

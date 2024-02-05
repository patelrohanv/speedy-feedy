from django import forms
from .models import SBI_Feedback, DESC_Feedback
from employees.models import Employee


class SBIFeedbackForm(forms.ModelForm):
    class Meta:
        model = SBI_Feedback
        fields = ["situation", "behavior", "impact", "provider", "receiver"]

    def __init__(self, *args, **kwargs):
        super(SBIFeedbackForm, self).__init__(*args, **kwargs)
        self.fields["provider"].queryset = Employee.objects.all()
        self.fields["receiver"].queryset = Employee.objects.all()
        self.fields["provider"].label_from_instance = (
            lambda obj: f"{obj.id}: {obj.last_name}, {obj.first_name}"
        )
        self.fields["receiver"].label_from_instance = (
            lambda obj: f"{obj.id}: {obj.last_name}, {obj.first_name}"
        )  # duplication, potential code smell


class DESCFeedbackForm(forms.ModelForm):
    class Meta:
        model = DESC_Feedback
        fields = [
            "describe",
            "explain",
            "specify",
            "consequences",
            "provider",
            "receiver",
        ]

    def __init__(self, *args, **kwargs):
        super(DESCFeedbackForm, self).__init__(*args, **kwargs)
        self.fields["provider"].queryset = Employee.objects.all()
        self.fields["receiver"].queryset = Employee.objects.all()
        self.fields["provider"].label_from_instance = (
            lambda obj: f"{obj.id}: {obj.last_name}, {obj.first_name}"
        )
        self.fields["receiver"].label_from_instance = (
            lambda obj: f"{obj.id}: {obj.last_name}, {obj.first_name}"
        )  # duplication, potential code smell

from django.shortcuts import render, redirect, get_object_or_404
from .forms import SBIFeedbackForm
from employees.models import Employee
from .models import SBI_Feedback


def add_sbi_feedback(request):
    if request.method == "POST":
        form = SBIFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("some_success_url")  # Redirect to a success page
    else:
        form = SBIFeedbackForm()

    return render(request, "feedback/add_sbi_feedback.html", {"form": form})


def list_sbi_feedback_provided(request, provider_id):
    provider = get_object_or_404(Employee, pk=provider_id)
    feedback_list = SBI_Feedback.objects.filter(provider=provider)
    context = {
        "provider": provider,
        "feedback_list": feedback_list,
    }
    return render(request, "feedback/list_sbi_feedback_provided.html", context)


def list_sbi_feedback_received(request, receiver_id):
    receiver = get_object_or_404(Employee, pk=receiver_id)
    feedback_list = SBI_Feedback.objects.filter(receiver=receiver)
    context = {
        "receiver": receiver,
        "feedback_list": feedback_list,
    }
    return render(request, "feedback/list_sbi_feedback_received.html", context)

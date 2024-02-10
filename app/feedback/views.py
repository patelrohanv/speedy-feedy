from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import SBIFeedbackForm, DESCFeedbackForm
from employees.models import Employee
from .models import SBI_Feedback, DESC_Feedback
from django.http import HttpResponseRedirect


def list_grow_feedback_received(request, receiver_id):
    return list_feedback(
        request,
        receiver_id,
        "grow",
        "feedback/list_grow_feedback_received.html",
        "receiver",
    )

def list_grow_feedback_provided(request, provider_id):
    return list_feedback(
        request,
        provider_id,
        "grow",
        "feedback/list_grow_feedback_provided.html",
        "provider",
    )

def add_grow_feedback(request):
    if request.method == 'POST':
        form = add_grow_feedback(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    else:
        form = add_grow_feedback()

    return render(request, "feedback/add_grow_feedback.html", {'form': form})


def feedback_success(request):
    feedback_type = request.GET.get("feedback_type", "")
    add_feedback_url = reverse(f"add_{feedback_type.lower()}_feedback")

    context = {
        "add_feedback_url": add_feedback_url,
    }
    return render(request, "feedback/feedback_success.html", context)


def add_sbi_feedback(request):
    if request.method == "POST":
        form = SBIFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            success_url = reverse("feedback_success") + "?feedback_type=SBI"
            return redirect(success_url)
    else:
        form = SBIFeedbackForm()

    return render(request, "feedback/add_sbi_feedback.html", {"form": form})


def add_desc_feedback(request):
    if request.method == "POST":
        form = DESCFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            success_url = reverse("feedback_success") + "?feedback_type=DESC"
            return redirect(success_url)
    else:
        form = DESCFeedbackForm()

    return render(request, "feedback/add_desc_feedback.html", {"form": form})


def list_sbi_feedback_provided(request, provider_id):
    return list_feedback(
        request,
        provider_id,
        SBI_Feedback,
        "feedback/list_sbi_feedback_provided.html",
        "provider",
    )

def list_sbi_feedback_received(request, receiver_id):
    return list_feedback(
        request,
        receiver_id,
        SBI_Feedback,
        "feedback/list_sbi_feedback_received.html",
        "receiver",
    )


def list_desc_feedback_provided(request, provider_id):
    return list_feedback(
        request,
        provider_id,
        DESC_Feedback,
        "feedback/list_desc_feedback_provided.html",
        "provider",
    )


def list_desc_feedback_received(request, receiver_id):
    return list_feedback(
        request,
        receiver_id,
        DESC_Feedback,
        "feedback/list_desc_feedback_received.html",
        "receiver",
    )


def list_feedback(request, employee_id, feedback_model, template_name, role):
    employee = get_object_or_404(Employee, pk=employee_id)
    if role == "provider":
        feedback_list = feedback_model.objects.filter(provider=employee)
    else:  # Assume 'receiver'
        feedback_list = feedback_model.objects.filter(receiver=employee)

    context = {
        "employee": employee,
        "feedback_list": feedback_list,
    }
    return render(request, template_name, context)


def list_all_feedback_provided(request, provider_id):
    provider = get_object_or_404(Employee, pk=provider_id)
    sbi_feedback_list = SBI_Feedback.objects.filter(provider=provider)
    desc_feedback_list = DESC_Feedback.objects.filter(provider=provider)

    context = {
        "provider": provider,
        "sbi_feedback_list": sbi_feedback_list,
        "desc_feedback_list": desc_feedback_list,
    }
    return render(request, "feedback/list_all_feedback_provided.html", context)


def list_all_feedback_received(request, receiver_id):
    receiver = get_object_or_404(Employee, pk=receiver_id)
    sbi_feedback_list = SBI_Feedback.objects.filter(receiver=receiver)
    desc_feedback_list = DESC_Feedback.objects.filter(receiver=receiver)

    context = {
        "receiver": receiver,
        "sbi_feedback_list": sbi_feedback_list,
        "desc_feedback_list": desc_feedback_list,
    }
    return render(request, "feedback/list_all_feedback_received.html", context)

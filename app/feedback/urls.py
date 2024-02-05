from django.urls import path
from .views import (
    add_sbi_feedback,
    list_sbi_feedback_provided,
    list_sbi_feedback_received,
)

urlpatterns = [
    path("sbi", add_sbi_feedback, name="add_sbi_feedback"),
    path(
        "sbi/provided/<int:provider_id>/",
        list_sbi_feedback_provided,
        name="list_sbi_feedback_provided",
    ),
    path(
        "sbi/received/<int:receiver_id>/",
        list_sbi_feedback_received,
        name="list_sbi_feedback_received",
    ),
]

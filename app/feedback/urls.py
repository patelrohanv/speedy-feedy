from django.urls import path
from .views import add_sbi_feedback, list_provided_feedback, list_received_feedback

urlpatterns = [
    path("", add_sbi_feedback, name="add_sbi_feedback"),
    path(
        "provided/<int:provider_id>/",
        list_provided_feedback,
        name="list_provided_feedback",
    ),
    path(
        "received/<int:receiver_id>/",
        list_received_feedback,
        name="list_received_feedback",
    ),
]

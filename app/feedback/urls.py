from django.urls import path
from .views import (
    feedback_success,
    add_sbi_feedback,
    add_desc_feedback,
    list_sbi_feedback_provided,
    list_sbi_feedback_received,
    list_desc_feedback_provided,
    list_desc_feedback_received,
    list_all_feedback_provided,
    list_all_feedback_received,
    list_grow_feedback_provided,
    add_grow_feedback,
    list_grow_feedback_received,
)

urlpatterns = [
    path("sbi/", add_sbi_feedback, name="add_sbi_feedback"),
    path("desc/", add_desc_feedback, name="add_desc_feedback"),
    path("grow/", add_grow_feedback, name="add_grow_feedback"),

    path("grow/received/<int:receiver_id>/",
        list_grow_feedback_received,
        name="list_grow_feedback_received",),
    
    path('grow/provided/<int:provider_id>/', 
         list_grow_feedback_provided, 
         name='list_grow_feedback_provided'),

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
    path(
        "desc/provided/<int:provider_id>/",
        list_desc_feedback_provided,
        name="list_desc_feedback_provided",
    ),
    path(
        "desc/received/<int:receiver_id>/",
        list_desc_feedback_received,
        name="list_desc_feedback_received",
    ),
    path("feedback_success/", feedback_success, name="feedback_success"),
    path(
        "provided/<int:provider_id>/",
        list_all_feedback_provided,
        name="list_all_feedback_provided",
    ),
    path(
        "received/<int:receiver_id>/",
        list_all_feedback_received,
        name="list_all_feedback_received",
    ),
]

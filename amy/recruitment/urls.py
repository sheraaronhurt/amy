from django.urls import include, path

from . import views

urlpatterns = [
    path(
        "process/add/<int:event_id>/",
        views.InstructorRecruitmentCreate.as_view(),
        name="instructorrecruitment_add",
    ),
    path(
        "process/<int:pk>/",
        include(
            [
                path(
                    "",
                    views.InstructorRecruitmentDetails.as_view(),
                    name="instructorrecruitment_details",
                ),
            ]
        ),
    ),
]

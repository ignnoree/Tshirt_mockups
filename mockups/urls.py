# mockups/urls.py
from django.urls import path
from django.http import JsonResponse
from .views import StartTaskAPIView, TaskStatusAPIView,MockupHistoryAPIView
from django.views.decorators.csrf import csrf_exempt
# Temporary test view
def test_view(request):
    return JsonResponse({"message": "Mockups app is working!"})

urlpatterns = [
    path("", test_view),
    path("tasks/start/", StartTaskAPIView.as_view(), name="start-task"),
    path("tasks/<str:task_id>/", TaskStatusAPIView.as_view(), name="task-status"),
    path("mockups/", MockupHistoryAPIView.as_view(), name="mockup-history")
]

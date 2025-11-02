from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from celery.result import AsyncResult
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from .tasks import generate_mockup
from .models import Mockup
from rest_framework.pagination import PageNumberPagination

# API view to start the celery task. 
class StartTaskAPIView(APIView):
    def post(self, request):
        text = request.data.get("text", "My T-Shirt")
        text_color=request.data.get("text_color", "#0000FF")
        print(text)
        task = generate_mockup.delay(text,text_color)
        return Response({"task_id": task.id, "status": "PENDING"}, status=status.HTTP_202_ACCEPTED)


# API view to check the status of an Celery task.
class TaskStatusAPIView(APIView):
    def get(self, request, task_id):
        ar = AsyncResult(task_id)
        response = {"task_id": task_id, "status": ar.status}
        if ar.status == "SUCCESS":
            response["result"] = ar.result  
        elif ar.status == "FAILURE":
            response["error"] = str(ar.result)
        return Response(response)


#retrieving created tshirts data 
class MockupHistoryAPIView(APIView):
    def get(self, request):
        mockups = Mockup.objects.all().order_by("-created_at")

        paginator = PageNumberPagination()
        paginator.page_size = 10  # optional (overrides settings.py)
        result_page = paginator.paginate_queryset(mockups, request)

        results = [
            {
                "id": m.id,
                "text": m.text,
                "image_url": m.image_url,
                "font": m.font,
                "text_color": m.text_color,
                "shirt_color": m.shirt_color,
                "created_at": m.created_at
            }
            for m in result_page
        ]
        return paginator.get_paginated_response(results)
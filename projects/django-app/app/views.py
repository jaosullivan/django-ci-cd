import os
import socket
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    context = {
        "app_name": "Django App",
        "pod_name": socket.gethostname(),
        "namespace": os.environ.get("POD_NAMESPACE", "unknown"),
        "version": os.environ.get("APP_VERSION", "dev"),
        "git_sha": os.environ.get("GIT_SHA", "unknown"),
        "health_status": "ok",
    }
    return render(request, "home.html", context)

def health(request):
    return JsonResponse({"status": "ok"})
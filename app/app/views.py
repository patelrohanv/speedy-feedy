from django.http import JsonResponse
from django.shortcuts import render


def home(request: "HttpRequest") -> "HttpResponse":
    return render(request, "index.html")


def health_check(request: "HttpRequest") -> "JsonResponse":
    return JsonResponse({"status": "OK"})

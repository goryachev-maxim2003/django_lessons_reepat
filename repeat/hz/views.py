from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .models import School

# Create your views here.
def number(request, num = "Число не передано"):
    return HttpResponse(f"{num}")
class Schools(View):
    """"Школы"""
    def get(self, request):
        schools = School.objects.all()
        return render(request, "main.html", {"schools": schools})

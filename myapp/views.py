from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    pounds = None

    if request.method == "POST":
        try:
            kilogram = float(request.POST.get("kilogram"))

            pounds = f"{kilogram}kg is equal to {kilogram * 2.20462}lb/s converted."
        except (ValueError, TypeError):
            pounds = "You have given an invalid value."

    return render(request, 'index.html', {'result': pounds})

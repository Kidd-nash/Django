from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    conversion_type = request.Get.get("convert")
    result = None

    if request.method == "POST":
        try:
            weight = float(request.POST.get("weight"))
            if conversion_type == "kg":
            elif conversion_type == "lb":
        except (ValueError, TypeError):
            pounds = "You have given an invalid value."

    return render(request, 'index.html', {'result': result})

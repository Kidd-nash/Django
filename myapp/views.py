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
                result = f"{weight} kg is equal to {round(weight * 2.20462, 2)} lb/s converted"
            elif conversion_type == "lb":
                result = f"{weight} lb/s is equal to {round(weight / 2.20462, 2)} kg converted"
        except (ValueError, TypeError):
            pounds = "You have given an invalid value."

    return render(request, "index.html", {
        "conversion_type": conversion_type,
        "result": result
    })

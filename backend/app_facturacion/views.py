from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def api_get_data(request):
    data = {"sucess": True, "message": "Data fetched successfully"}
    return JsonResponse(data)
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'story/world_map.html')

def home_page(request):
    return HttpResponse('I am just adding a world map')
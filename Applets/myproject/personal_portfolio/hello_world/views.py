from django.shortcuts import render

def hello_world(request):
    return render(request, 'hello_world.html', {})# Each function or class handles the logic that gets processed each time a different URL is visited.

# Create your views here. 

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
import threading
import pandas as pd


# Create your views here.
#request->response
#request handler
#action
@csrf_exempt
def say_hello(request):
    df = pd.read_excel('cities_list.xlsx')
    cities = list(df['name'])
    return render(request, 'main.html', {'name': 'Jineet', 'cities': cities})


@csrf_exempt
def handle_form(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        location = request.POST.get('dropdown')
        min_temp = request.POST.get('minTemp')
        max_temp = request.POST.get('maxTemp')

        # Create a new thread that will run the os.system call
        thread = threading.Thread(
            target=os.system,
            args=(
                f'python agent.py {email} "{location}" {min_temp} {max_temp}',
            ))
        # Start the new thread
        thread.start()

        return render(
            request, 'results.html', {
                'email': email,
                'location': location,
                'min_temp': min_temp,
                'max_temp': max_temp
            })

from django.shortcuts import render
import json
import urllib.request
import os

# Create your views here.

def index(request):
    data = {}  
    city = ""
    if request.method == 'POST':
        city = request.POST["city"]
        try:
            # Use the API key from environment variables
            api_key = os.getenv("API_KEY")
            res = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}').read()
            json_data = json.loads(res)
            data = {
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) + ', ' + str(json_data['coord']['lat']),
                "temp": str(json_data['main']['temp']) + ' K',  
                "pressure": str(json_data['main']['pressure']),  
                "humidity": str(json_data['main']['humidity']),  
            }
            
        except Exception as e:
            data['error'] = str(e)  
        
    return render(request, 'index.html', {'city': city, 'data': data})

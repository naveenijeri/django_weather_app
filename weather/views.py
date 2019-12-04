from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=aca7104c3bd8d937fcce842f5600f00e'
    if request.method=="POST":
        #print(request.POST)

      form=CityForm(request.POST)
      form.save()
    form=CityForm()

    cities=City.objects.all()
    weather_data=[]

    for city in cities:
        r = requests.get(url.format(city)).json()
        print(r)
        F=r['main']['temp']
        temperature=((F-32)*5)/9
        temp=round(temperature,2)



        city_weather={
            'city':city.name,
            'temperature':temp,
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],

        }
        weather_data.append(city_weather)
    #print(weather_data)
    context={'weather_data':weather_data,'form':form}


    return render(request,'weather/weather.html',context)


from requests import get
from pyfiglet import figlet_format

print(figlet_format("WEATHER REPORT"))  # prints title

loop = 'yes'
while loop == "y" or loop == "yes":
    api_key = "*****************************"  # key used to access websites API
    city = input("What city do you live in: ")  # user inputs a city for the website to use
    # f string as the URL that changes based on the city
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    res = get(url)  # requests the information of the URL

    if res.status_code == 200:
        data = res.json()  # changes the information to accessible python

        weather = data["weather"][0]["description"]  # creates a variable for the description of the weather
        # temp is a dict of all the relevant data converted to Fahrenheit
        temp = {"Temperature": round((data["main"]["temp"] - 273.15) * 9 / 5 + 32, 2),
                "Feels like": round((data["main"]["feels_like"] - 273.15) * 9 / 5 + 32, 2),
                "High": round((data["main"]["temp_max"] - 273.15) * 9 / 5 + 32, 2),
                "Low": round((data["main"]["temp_min"] - 273.15) * 9 / 5 + 32, 2),
                "Humidity": round((data["main"]["humidity"]))
                }

        print(f'Temperature(Fahrenheit): {temp["Temperature"]}')
        print(f'Feels like: {temp["Feels like"]}')
        print(f'High: {temp["High"]}')
        print(f'Low: {temp["Low"]}')
        print(f'Humidity: {temp["Humidity"]}%\n')
        print(f'description: {weather}\n')
    else:
        print("error: could not load location.")

    loop = input("Would you like to go again ('yes' or 'no'):")

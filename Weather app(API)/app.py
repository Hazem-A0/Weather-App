from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = '4645ff4a6889bf7cc20f2062d9802bbf'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        units = 'metric'  
        weather_data = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}')
        
        if weather_data.status_code == 200:
            weather = weather_data.json()['weather'][0]['main']
            temperature = round(weather_data.json()['main']['temp'])
            humidity = weather_data.json()['main']['humidity']
            unit_symbol = 'C' if units == 'metric' else 'F' if units == 'imperial' else 'K'
            return render_template('index.html', weather=weather, temperature=temperature,humidity=humidity,city=city, unit_symbol=unit_symbol)
        else:
            error = "City not found"
            return render_template('index.html', error=error)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

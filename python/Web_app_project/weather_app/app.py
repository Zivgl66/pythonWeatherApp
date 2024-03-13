from flask import Flask, render_template, request
from utils.funcs import get_weekday, validate_input
from modules.api_calls import get_weather
from deep_translator import GoogleTranslator

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# app.jinja_env.globals.update(get_weather=get_weather)


@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template('index.html')
	if request.method == 'POST':
		location = request.form['location']
		validate = validate_input(location)
		if validate != 'OK':
				return render_template('index.html', validate=validate)
		else:
			data = get_weather(location)
			if data != 400:
				days_list = get_weekday(data)
				country = data['resolvedAddress'].split(",")[-1]
				country = GoogleTranslator(source='auto', target='en').translate(country)
				return render_template('index.html', data=data,country=country, days_list=days_list)
			else:
				not_found = "Location Not Found!"
				return render_template('index.html', not_found=not_found)


if __name__ == '__main__':
    app.run()
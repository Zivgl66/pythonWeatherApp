from flask import Flask, render_template, request
from utils.funcs import get_weekday, validate_input, translate
from modules.api_calls import get_weather

"""
	This a weather app built using flask. 
	there is a single page application, using the home route '/'.
	by entering input, after validation, we GET req
 	the api for the locations weather info and render 
  	it to the user.
"""

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True #reload when template chages



@app.route('/', methods=['GET', 'POST'])
def home():
    # The method renders the html template with the variables depending on validation and api call results
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
				country = translate(country)
				return render_template('index.html', data=data,country=country, days_list=days_list)
			else:
				not_found = "Location Not Found!"
				return render_template('index.html', not_found=not_found)


if __name__ == '__main__':
    app.run()
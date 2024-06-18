from flask import Flask, render_template, request, redirect, session, url_for, flash, jsonify, send_from_directory
from flask_cors import CORS
from utils.funcs import get_weekday, validate_input, translate, validate_user, signup_user, login_user
from modules.db import add_user_to_db, login_user_from_db
from modules.api_calls import get_weather, save_query
from datetime import timedelta
import os
import logging
from prometheus_client import Counter, CONTENT_TYPE_LATEST, generate_latest, Gauge


# Logs for filebeat
logger = logging.getLogger(__name__)


#   Metrics for prometheus
# Create a counter metric to count requests
request_count = Counter('http_req_total', 'HTTP Requests Total')
# Create a gauge metric to measure system memory usage
memory_usage = Gauge('memory_usage_in_bytes', 'System Memory Usage')
# Create a counter to see how many time a city was searched
city_counter = Counter('city_search_total', 'City Search Total', ['location'])

"""
    This a weather app built using flask. 
    there is a single page application, using the home route '/'.
    by entering input, after validation, we GET req
    the api for the locations weather info and render 
    it to the user.
    
    CR: Maxim Cherepanov
"""

app = Flask(__name__)
CORS(app)
app.config["TEMPLATES_AUTO_RELOAD"] = True  # reload when template chages
app.secret_key = "asdsadsadsaaewqewqrfdgvdfas"
app.permanent_session_lifetime = timedelta(seconds=3600)

background_color = os.getenv('BG_COLOR', '#FFFFFF')
print("bg color: ", background_color)



@app.route('/', methods=['GET', 'POST'])
def root():
        request_count.inc()
        logging.basicConfig(filename='./logs/app_logs.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger.setLevel(logging.INFO)
        logger.warning('Someone has logged in')
        return redirect('/login', code=302)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        request_count.inc()
        if "user" not in session:
            logging.basicConfig(filename='./logs/app_logs.log', level=logging.CRITICAL, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logger.setLevel(logging.CRITICAL)
            # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            
            logger.critical('Someone wants to signup')
            return render_template('signup.html',background_color=background_color)
        else:
            return redirect('/home', code=302)
    if request.method == 'POST':
        request_count.inc()
        username = request.form['username']
        password = request.form['password']
        if add_user_to_db(username, password) is False:
        #if validate_user(username):
            info = "User already exists or inccorect"
            logging.basicConfig(filename='./logs/app_logs.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logger.setLevel(logging.DEBUG)
            logger.warn('Failed Sinup')
            return render_template('signup.html', info=info ,background_color=background_color)
        else:
            #signup_user(username, password)
            return redirect('/login', code=302)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        request_count.inc()
        if "user" in session:
            return redirect('/home', code=302)
        logging.basicConfig(filename='./logs/app_logs.log', level=logging.WARNING, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger.setLevel(logging.WARNING)
        logger.warning('Someone wants to login')
        return render_template('login.html',background_color=background_color)
    if request.method == 'POST':
        request_count.inc()
        session.permanent = True
        username = request.form['username']
        password = request.form['password']
        info = "Invalid Username or Password"
        if login_user_from_db(username, password):
        #if login_user(username, password):
            # flash('You were successfully logged in')
            session["user"] = username
            return redirect('/home', code=302)
        else:
            logging.basicConfig(filename='./logs/app_logs.log', level=logging.WARN, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logger.setLevel(logging.WARN)
            logger.warn('Failed Login')
            return render_template('login.html', info=info ,background_color=background_color)


@app.route('/home', methods=['GET', 'POST'])
def home():
    # The method renders the html template with the variables depending on validation and api call results
    if request.method == 'GET':
        request_count.inc()
        if "user" in session:
            logging.basicConfig(filename='./logs/app_logs.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logger.setLevel(logging.INFO)
            logger.warning('Someone has logged in')
            return render_template('index.html',background_color=background_color)
        return redirect('/login', code=302)
    if request.method == 'POST' and "user" in session:
        request_count.inc()
        location = request.form['location']
        city_counter.labels(location=location).inc()
        validate = validate_input(location)
        if validate != 'OK':
            return render_template('index.html', validate=validate,background_color=background_color)
        else:
            data = get_weather(location)
            if data != 400:
                days_list = get_weekday(data)
                country = data['resolvedAddress'].split(",")[-1]
                country = translate(country)
                save_query(country, data)
                return render_template('index.html', data=data, country=country, days_list=days_list ,background_color=background_color)
            else:
                not_found = "Location Not Found!"
                return render_template('index.html', not_found=not_found ,background_color=background_color)
    else:
        return redirect('/login', code=302)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'GET':
        request_count.inc()
        session.pop("user", None)
        return redirect(url_for("login"))


@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}


@app.route('/history')
def history():
    # Directory where saved query files are stored
    directory = 'data'
    
    # Get a list of files in the directory
    files = os.listdir(directory)
    
    # Render HTML template with the list of files
    return render_template('history.html', files=files )

@app.route('/download/<path:filename>')
def download_file(filename):
    # Directory where saved query files are stored
    directory = 'data'
    
    # Serve the requested file for download
    return send_from_directory(directory, filename)

@app.errorhandler(404)
def page_not_found(e):
    request_count.inc()
    return jsonify({"status": 404, "message": "Not Found"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0')

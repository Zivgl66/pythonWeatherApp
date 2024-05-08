from flask import Flask, render_template, request, redirect, session, url_for, flash, jsonify
from flask_cors import CORS
from utils.funcs import get_weekday, validate_input, translate, validate_user, signup_user, login_user
from modules.db import add_user_to_db, login_user_from_db
from modules.api_calls import get_weather
from datetime import timedelta
import os
import logging


logger = logging.getLogger(__name__)

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
app.secret_key = os.urandom(30)
app.permanent_session_lifetime = timedelta(seconds=15)


@app.route('/', methods=['GET', 'POST'])
def root():
        logging.basicConfig(filename='./logs/app_logs.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger.setLevel(logging.INFO)
        logger.warning('Someone has logged in')
        return redirect('/login', code=302)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        if "user" not in session:
            logging.basicConfig(filename='./logs/app_logs.log', level=logging.CRITICAL, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logger.setLevel(logging.CRITICAL)
            # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            
            logger.critical('Someone wants to signup')
            return render_template('signup.html')
        else:
            return redirect('/home', code=302)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if add_user_to_db(username, password) is False:
        #if validate_user(username):
            info = "User already exists or inccorect"
            logging.basicConfig(filename='./logs/app_logs.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logger.setLevel(logging.DEBUG)
            logger.warn('Failed Sinup')
            return render_template('signup.html', info=info)
        else:
            #signup_user(username, password)
            return redirect('/login', code=302)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if "user" in session:
            return redirect('/home', code=302)
        logging.basicConfig(filename='./logs/app_logs.log', level=logging.WARNING, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger.setLevel(logging.WARNING)
        logger.warning('Someone wants to login')
        return render_template('login.html')
    if request.method == 'POST':
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
            return render_template('login.html', info=info)


@app.route('/home', methods=['GET', 'POST'])
def home():
    # The method renders the html template with the variables depending on validation and api call results
    if request.method == 'GET':
        if "user" in session:
            logging.basicConfig(filename='./logs/app_logs.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logger.setLevel(logging.INFO)
            logger.warning('Someone has logged in')
            return render_template('index.html')
        return redirect('/login', code=302)
    if request.method == 'POST' and "user" in session:
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
                return render_template('index.html', data=data, country=country, days_list=days_list)
            else:
                not_found = "Location Not Found!"
                return render_template('index.html', not_found=not_found)
    else:
        return redirect('/login', code=302)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'GET':
        session.pop("user", None)
        return redirect(url_for("login"))


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0')

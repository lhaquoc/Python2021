import os

from cs50 import SQL
from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
from flask_caching import Cache
from flask_cors import CORS

app = Flask(__name__)

# send mail configurations
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
mail = Mail(app)

# CORS config
cors = CORS()
cors.init_app(app)

# db configuration
db = SQL('sqlite:///froshims.db')
# caching
cache = Cache()
cache.init_app(app)

SPORTS = [
    "Dodge-ball",
    "Flag football",
    "Soccer",
    "Ultimate Frisbee",
    "Basket ball"
]


@app.route('/', methods=['GET', 'POST'])
def index():  # put application's code here
    cache.clear()
    return render_template('index.html', sports=SPORTS)


@app.route('/deregister', methods=['POST'])
def deregister():
    id = request.form.get('id')
    if id:
        db.execute('DELETE FROM registrants WHERE  id = ?', id)
    return redirect('/registrants')


@app.route('/register', methods=['POST'])
def register():
    # name and sport validation
    email = request.form.get('email')
    sport = request.form.get('sport')
    if not email:
        return render_template('error.html', message='Missing email')
    if not sport:
        return render_template('error.html', message='Missing sport')
    if sport not in SPORTS:
        return render_template('error.html', message='Invalid sport')

    # remember registrant
    db.execute('INSERT INTO registrants (email, sport) VALUES(?, ?)', email, sport)
    # send email
    message = Message('You are registered!', recipients=[email])
    mail.send(message)
    # confirm registration
    return redirect('/registrants')


@app.route('/registrants')
def registrants():
    registrants = db.execute('SELECT * FROM registrants')
    return render_template('registrants.html', registrants=registrants)


@app.route('/profiles')
def profiles():
    registrants = db.execute('SELECT * FROM registrants')
    return registrants


if __name__ == '__main__':
    app.run()

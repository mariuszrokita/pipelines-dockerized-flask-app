from flask import Flask
from os import environ

app = Flask(__name__)

# Load configuration from environment variable pointing to configuration file
app.config.from_envvar('APP_SETTINGS')
app.config.from_ob

print(environ)

print(app.config['TEXT_TO_DISPLAY'])

# Load config value directly from environment variable
app.config['STRIPE_API'] = environ.get('STRIPE_API_KEY')


@app.route('/')
def index():
    return f"<h1>{app.config['STRIPE_API']}</h1>"

if __name__ == '__main__':
    app.run(port=5000, use_reloader=False, host='0.0.0.0')

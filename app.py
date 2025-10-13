from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Die Küche der Rezeptfreundin ist geöffnet und bereit für Anfragen!"

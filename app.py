from flask import Flask
import os

app = Flask(__name__)

# This loads the beautiful website
with open('index.html','r',encoding='utf-8') as f:
    HTML = f.read()

@app.route('/')
def home():
    return HTML

if __name__ == '__main__':
    app.run(debug=True, port=5000)
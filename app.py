
# TOKEN = "bi6gUr6cX58R9Y3A17Km8bqM8vag6liLl9ETbuxl0de41b76"
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Замените 'YOUR_API_KEY' на ваш реальный API ключ
API_KEY = 'bi6gUr6cX58R9Y3A17Km8bqM8vag6liLl9ETbuxl0de41b76'

@app.route('/')
def index():
    quote = get_random_quote()
    return render_template('index.html', quote=quote)

def get_random_quote():
    url = f"https://quotes.rest/qod?apiKey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        quote = data["contents"]["quotes"][0]["quote"]
        author = data["contents"]["quotes"][0].get("author", "Unknown")
        return {"quote": quote, "author": author}
    else:
        return {}

if __name__ == "__main__":
    app.run(debug=True)
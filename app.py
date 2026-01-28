from flask import Flask, request, redirect, render_template
import string, random

app = Flask(__name__)

# Temporary database (dictionary)
url_db = {}

def generate_code(length=5):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_code = generate_code()

        url_db[short_code] = long_url
        short_url = request.host_url + short_code

        return render_template('index.html', short_url=short_url)

    return render_template('index.html', short_url=None)

@app.route('/<code>')
def redirect_url(code):
    long_url = url_db.get(code)
    if long_url:
        return redirect(long_url)
    return "Invalid URL"

if __name__ == "__main__":
    app.run(debug=True)

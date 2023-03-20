from flask import Flask, render_template, url_for, redirect, request, session, flash
import requests

app = Flask(__name__)

app.secret_key = 'abcd1234'

@app.route("/", methods=['GET'])
def index():
    if "user" in session:
        # Ambil data dari API
        try:
            data = requests.get('https://backend-risna-5zn7xh2gqq-et.a.run.app/products')
        except Exception as e:
            print("ERROR | Get products data |", e)

        return render_template("index.html", user=session["user"], products=data.json())
    else:
        return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Ambil data dari API
        try:
            users = requests.get('https://backend-risna-5zn7xh2gqq-et.a.run.app/users')
        except Exception as e:
            print("ERROR | Get products data |", e)

        for user in users.json():
            if user["username"] == username:
                if password == user['password']:
                    session["user"] = user["name"]
                    return redirect(url_for('index'))
                else:
                    flash("Login failed", category='error')
            else:
                flash('Username not registered', category='error')
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
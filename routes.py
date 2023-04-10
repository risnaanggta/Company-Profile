from flask import Flask, render_template, url_for, redirect, session
app = Flask(__name__) 
#app.config["SECRET_KEY"] = "risnaanggta"     

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/service")
def service():
  return render_template("service.html")

@app.route("/menu")
def menu():
  return render_template("menu.html")

@app.route("/booking")
def booking():
  return render_template("booking.html")

@app.route("/team")
def team():
  return render_template("team.html")

@app.route("/testimonial")
def testimonial():
  return render_template("testimonial.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")

if __name__ == '__main__':
  app.run(debug=True)
from flask import Flask, request, redirect, url_for, session, render_template, flash
import requests


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

@app.route("/booking", methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
            # Ambil data produk dari form
          nama = request.form['nama']
          notelp = request.form['notelp']
          tanggal = request.form['tanggal']
          people = request.form['people']
          pesan = request.form['pesan']
            

            # Buat data JSON yang berisi informasi produk yang akan ditambahkan
          data = {"nama": nama, "notelp": notelp, "tanggal": tanggal, "people": people, "pesan": pesan }

            # Kirim request POST ke API produk
          try:
              response = requests.post('https://backend-risna-5zn7xh2gqq-et.a.run.app/booking', json=data)
              if response.status_code == 201:
                  print("Reservasi added successfully")
              else:
                  print("ERROR | Add product |", response.status_code)
          except Exception as e:
                print("ERROR | Add product |", e)
    else:
        print("ERROR | Add product |", "Invalid request method")
    return render_template("booking.html")

@app.route("/team")
def team():
  return render_template("team.html")

@app.route("/testimonial", methods=['GET', 'POST'])
def testimonial():
    if request.method == 'POST':
            # Ambil data produk dari form
          nama = request.form['nama']
          testimoni = request.form['testimoni']
            

            # Buat data JSON yang berisi informasi produk yang akan ditambahkan
          data = {"nama": nama, "testimoni": testimoni }

            # Kirim request POST ke API produk
          try:
              response = requests.post('https://backend-risna-5zn7xh2gqq-et.a.run.app/addtestimoni', json=data)
              if response.status_code == 201:
                  print("Testimoni added successfully")
              else:
                  print("ERROR | Add product |", response.status_code)
          except Exception as e:
                print("ERROR | Add product |", e)
    else:
        print("ERROR | Add product |", "Invalid request method")
    return render_template("testimonial.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")

if __name__ == '__main__':
  app.run(debug=True)

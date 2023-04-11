import falcon, jwt
import json
import psycopg2
from waitress import serve
from connectdb import conn

from API.booking import Booking
from API.testimoni import ReadTestimoni, AddTestimoni




# buat middleware jika ingin mengakses halaman harus login terlebih dahulu
 

# Inisialisasi aplikasi Falcon
app = falcon.API()

# Tambahkan route untuk login dan halaman terproteksi
app.add_route('/booking', Booking())
app.add_route('/testimoni', ReadTestimoni())
app.add_route('/addtestimoni', AddTestimoni())
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)
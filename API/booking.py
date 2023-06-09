import falcon, jwt
from datetime import datetime, timedelta, timezone


from query.booking import query_booking


class Booking:
   def on_post(self, req, resp):
      nama = req.media.get('nama') 
      notelp = req.media.get('notelp') 
      tanggal = req.media.get('tanggal') 
      people = req.media.get('people') 
      pesan = req.media.get('pesan') 
         
      if not nama or not notelp or not tanggal or not people or not pesan:
         resp.status = falcon.HTTP_BAD_REQUEST
         return
      user = query_booking(nama, notelp, tanggal, people, pesan)
      if user is True:
         resp.status = falcon.HTTP_200
         resp.media = {'message': 'Berhasil Reservasi'}
      else:
         resp.status = falcon.HTTP_401
         resp.media = {'message': 'Gagal Reservasi'}
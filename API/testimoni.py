import falcon, jwt
from datetime import datetime, timedelta, timezone


from query.testimoni import query_testimoni


class Booking:
   def on_post(self, req, resp):
      nama = req.media.get('nama') 
      testimoni = req.media.get('testimoni') 
      
      if not nama or not testimoni:
         resp.status = falcon.HTTP_BAD_REQUEST
         return
      user = query_testimoni(nama, testimoni)
      if user is True:
         resp.status = falcon.HTTP_200
         resp.media = {'message': 'Berhasil Memberi Penilaian'}
      else:
         resp.status = falcon.HTTP_401
         resp.media = {'message': 'Gagal Memberi Penilaian'}
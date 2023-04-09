import falcon, jwt 
from datetime import datetime, timedelta, timezone


from query.testimoni import query_testimoni


class Testimoni:
   def on_post(self, req, resp):
      id = req.media.get('id') 
      nama = req.media.get('nama') 
      testimoni = req.media.get('testimoni') 
      
      if not id or not nama or not testimoni:
         resp.status = falcon.HTTP_BAD_REQUEST
         return
      
      user = query_testimoni(id, nama, testimoni)

      if user is True:
         resp.status = falcon.HTTP_200
         resp.media = {'message': 'Berhasil memberi testimoni'}
      else:
         resp.status = falcon.HTTP_401
         resp.media = {'message': 'Gagal memberi testimoni'}

   def on_delete(self, resp, id):
      user = query_testimoni(id)
      if user is True:
         resp.status = falcon.HTTP_204
         resp.media = {'message': 'Berhasil menghapus testimoni'}
      else:
         resp.status = falcon.HTTP_404
         resp.media = {'message': 'Gagal menghapus testimoni'}


   def on_put(self, req, resp):
      id = req.media.get('id') 
      nama = req.media.get('nama') 
      testimoni = req.media.get('testimoni') 
         
      if not id or not nama or not testimoni:
         resp.status = falcon.HTTP_BAD_REQUEST
         return
      
      updated = query_testimoni(id, nama, testimoni)
      
      if updated is True:
         resp.status = falcon.HTTP_200
         resp.media = {'message': 'Testimoni berhasil diperbarui'}
      else:
         resp.status = falcon.HTTP_404
         resp.media = {'message': 'Gagal memperbarui testimoni'}
import falcon, jwt
from datetime import datetime, timedelta, timezone


from query.testimoni import query_get_all_testimonial, query_add_testimoni


class ReadTestimoni:
   def on_get(self, req, resp):
        testimonial = query_get_all_testimonial()
        if testimonial:
            resp.media = {"testimoni": testimonial}
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_404
            resp.media = {'message': 'Testimoni not found'}

class AddTestimoni:
   def on_post(self, req, resp): 
        nama = req.media.get('nama') 
        komentar = req.media.get('komentar') 

        if not nama or not testimoni:
            resp.status = falcon.HTTP_BAD_REQUEST
            return
        testimoni = query_add_testimoni(nama, testimoni)
        if testimoni is True:
            resp.status = falcon.HTTP_200
            resp.media = {'message': 'Add testimoni berhasil'}
        else:
            resp.status = falcon.HTTP_401
            resp.media = {'message': 'Add testimoni gagal'}


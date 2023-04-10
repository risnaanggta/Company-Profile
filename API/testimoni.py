import falcon, jwt
from datetime import datetime, timedelta, timezone


from query.testimoni import query_get_all_testimoni, query_add_testimoni, query_delete_testimoni, query_update_testimoni, query_get_testimoni_by_id


class ReadTestimoni:
   def on_get(self, req, resp):
        testimoni = query_get_all_testimoni()
        if testimoni:
            resp.media = {"testimoni": testimoni}
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_404
            resp.media = {'message': 'Testimoni not found'}

class AddTestimoni:
   def on_post(self, req, resp): 
        nama = req.media.get('nama') 
        testimoni = req.media.get('testimoni') 

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


class DeleteTestimoni:
    def on_delete(self, req, resp):
        nama = req.media.get('id')
        if not nama:
            resp.status = falcon.HTTP_BAD_REQUEST
            return
        testimoni = query_delete_testimoni(nama)
        if testimoni is True:
            resp.status = falcon.HTTP_200
            resp.media = {'message': 'Delete testimoni berhasil'}
        else:
            resp.status = falcon.HTTP_401
            resp.media = {'message': 'Delete testimoni gagal'}


class UpdateTestimoni :
    def on_put(self, req, resp):
        nama = req.media.get('nama') 
        testimoni = req.media.get('testimoni')
        id = req.media.get('id') 
       
        testimoni = req.media.get('id')
        if not nama or not testimoni:
            resp.status = falcon.HTTP_BAD_REQUEST
            return
        testimoni = query_update_testimoni(nama, testimoni, id)
        if testimoni is True:
            resp.status = falcon.HTTP_200
            resp.media = {'message': 'Update testimoni berhasil'}
        else:
            resp.status = falcon.HTTP_401
            resp.media = {'message': 'Update testimoni gagal'}

class GetTestimoniById:
    def on_post(self, req, resp):
        id = req.media.get('id')
        if not id:
            resp.status = falcon.HTTP_BAD_REQUEST
            return
        testimoni = query_get_testimoni_by_id(id)
        if testimoni:
            resp.status = falcon.HTTP_200
            resp.media = { 'testimoni': testimoni}
        else:
            resp.status = falcon.HTTP_401
            resp.media = {'message': 'Testimoni not found'}
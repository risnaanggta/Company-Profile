import falcon
import connDB

class Products:
    def on_get(self, req, resp):
        data = [ # Proses ini (nantinya) diganti dengan query ke database
            {'pid': 'AQ600', 'sid': 'DNN', 'name': 'Aqua 600 ml', 'type': 'Drink', 'stock': 1000},
            {'pid': 'LM600', 'sid': 'LMI', 'name': 'Le Minerale 600 ml', 'type': 'Drink', 'stock': 750},
            {'pid': 'AD600', 'sid': 'ADS', 'name': 'Ades 600 ml', 'type': 'Drink', 'stock': 1500},
        ]
        resp.media = data
        resp.status = falcon.HTTP_200

class Users:
    def on_get(self, req, resp):
        users = [
            {'username': 'admin', 'name': 'Admin', 'password': 'admin123'},
        ]
        resp.media = users
        resp.status = falcon.HTTP_200

class GetPrice:
    def on_get(self, req, resp):
        query = "SELECT current_date"
        data = connDB.select()

        resp.media = data
        resp.status = falcon.HTTP_200


app = falcon.App()

app.add_route('/products', Products())
app.add_route('/users', Users())
app.add_route("/price", GetPrice())

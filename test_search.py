import xmlrpc.client
from xmlrpc.client import Fault

db = "test"
username = "test@mail.com"
password = ""
url = "http://localhost:8076"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

info = models.execute_kw(
    db
    , uid
    , password
    , 'stock.picking'
    , 'search'
    , [
        [
            [
                'picking_type_id', '=', 1
            ]
        ]
    ]
)

print(str(info))

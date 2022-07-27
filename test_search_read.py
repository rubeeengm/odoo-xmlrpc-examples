import xmlrpc.client
from xmlrpc.client import Fault

db = 'test'
username = 'test@mail.com'
password = ''
url = 'http://localhost:8076'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

# autenticamos
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

info = models.execute_kw(
    db
    , uid
    , password
    , 'stock.picking'
    , 'search_read'
    , [
        [
            # '|'
            # , [
            #     'id', '=', 9
            # ] ,
            [
                'id', '=', 36
            ]
        ]
    ]
    , {
        'fields': [
            'id', 'name', 'state', 'scheduled_date', 'move_line_ids', 'move_lines'
        ]
    }
)

print(str(info))

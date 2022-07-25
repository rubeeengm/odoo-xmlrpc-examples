import xmlrpc.client
from xmlrpc.client import Fault

db = 'test'
username = 'test@mail.com'
password = ""
url = 'http://localhost:8076'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

info = models.execute_kw(
    db
    , uid
    , password
    , 'stock.picking'
    , 'create'
    , [
        {
            'partner_id': 14,
            'picking_type_id': 1,
            'location_id': 4,
            'location_dest_id': 8,
            'scheduled_date': '2022-07-25 05:08:03',
            'origin': False,
            'package_level_ids': [],
            'move_type': 'direct',
            'user_id': uid,
            'note': 'Example2',
            'move_ids_without_package':[
                (
                    0
                    , 0
                    , {
                        # "name": "[DESK0005] Customizable Desk (CONFIG) (Custom, White)",
                        'state': 'draft',
                        'picking_type_id': 1,
                        'location_id': 4,
                        'location_dest_id': 8,
                        'product_id': 38,
                        # "product_uom": 1,
                        'quantity_done': 1
                    }
                )
            ]
        }
    ]
)

print(str(info))

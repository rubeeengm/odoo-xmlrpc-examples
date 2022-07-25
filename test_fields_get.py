import xmlrpc.client
from xmlrpc.client import Fault

db = "test"
username = "test@mail.com"
password = ""
url = "http://localhost:8076"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, username, password, {})

# print('uid:', uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# print('models:', models)

fields = None

try:
    fields = models.execute_kw(
        db
        , uid
        , password
        , 'stock.picking'
        , 'fields_get'
        , []
        , {
            'attributes': [
                'string', 'help', 'type'
            ]
        }
    )
except Exception as e:
# except Fault as e:
    # print('fault_code: ', e.faultCode)
    # print('fault_string: ', e.faultString)
    print(e)


if fields:
    print(str(fields))

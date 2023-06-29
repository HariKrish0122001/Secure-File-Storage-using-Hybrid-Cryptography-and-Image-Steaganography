import json
import os,io,sys
from zcatalyst import datastore
import zcatalyst

os.environ['CATALYST_AUTH'] = json.dumps(
    {'refresh_token': '1000.0e2f9bdcf8f047882cad13bdb99f4a49.c70f107fc82f39ec6dcbda5a65fca219',
     'client_id': '1000.HN38DZYCSYQ8TU588BQ97RW44GSAMK',
     'client_secret': '4740ebde1bdcb3d7c3d14193fcdffe8a9f7864196c'
     })
os.environ['CATALYST_OPTIONS'] = json.dumps(
    {'project_id': '5249000000008013', 'project_key': '1008807534',
     'project_domain': 'https://sample-71779596.development.localcatalystserverless.com'
     })

zcatalyst.initialize_app()
datastore=datastore.instance()
# print(datastore.get_all_tables())
test_table=datastore.get_all_tables()[0]
# print(test_table)
test_table_id=test_table._identifier
print(type(datastore.get_table_details(test_table_id)))
test_table=datastore.table(test_table_id)
# print(test_tabl1)
# print(test_table.get_all_columns()[-1])
# column_id=test_table.get_all_columns()[-1]['column_id']
# print(test_table.get_all_columns()[-1])
column_id=test_table.get_all_columns()[-1]['column_id']
# print(test_table.get_column_details(column_id))
# print(test_table.insert_row({"notes":"test"}))
# row_id=test_table.insert_row({"notes":"test"})['ROWID']
# print(test_table.get_row(row_id))
# print(test_table.update_row({'notes': 'notes','ROWID': row_id}))
# print(test_table.get_paged_rows()['data'][0]["notes"])
print(test_table.get_iterable_rows())
# print(obj)
# row_response=test_table.insert_rows([{"notes":"test1"},{"notes":"test2"}])
# print(row_response[0]['ROWID'])
# row_id1 = row_response[0]["ROWID"]
# row_id2 = row_response[1]["ROWID"]
# row_response=test_table.update_rows([{'notes': 'notes1','ROWID': row_id1},{'notes': 'notes2','ROWID': row_id2}])
# print(row_response)
# delete_response=test_table.delete_rows([row_id1,row_id2])
# print(delete_response)
# print(test_table.delete_row(row_id))

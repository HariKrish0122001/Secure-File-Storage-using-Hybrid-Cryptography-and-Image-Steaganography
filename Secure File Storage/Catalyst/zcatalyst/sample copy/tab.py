import json
from operator import le, ne
import os
from urllib import response
import zcatalyst
from zcatalyst import datastore,zcql


os.environ['CATALYST_AUTH'] = json.dumps({'refresh_token':'1000.f35e6e66dd7d67f7894109b892191337.2383ad214d378eb82fa2622837a2b24c',
                                          'client_id':'1000.HN38DZYCSYQ8TU588BQ97RW44GSAMK',
                                          'client_secret':'4740ebde1bdcb3d7c3d14193fcdffe8a9f7864196c'})
os.environ['CATALYST_OPTIONS'] = json.dumps({'project_id':'5249000000008013','project_key':'1008807534','project_domain':'https://sample-71779596.development.localcatalystserverless.com'})

zcatalyst.initialize_app()
datastore=datastore.instance()
#zcql=zcql.instance()
all_segment_details = datastore.get_all_tables()
#print(cache.get_all_segment)
#print(all_segment_details)
#cache.segment(id="123")
"""for i in range(1,len(all_segment_details)+1):
    print(f'Segment {i} id = ' + str(all_segment_details[i-1][table_name]))"""
#d2=datastore.table('5249000000011745')
#d2.delete_row('5249000000015476')
"""details=d2.get_all_columns()
for i in range(len(details)):
    #print(f"Column{i}",details[i-1])
    #print(type(details))
    #y = json.loads(details[i].text)
    y=details[i]
    print(y['column_name'])
"""
#d2.insert_row({'col_test1':"aa"})
#print(d2)
#print(datastore.get_all_tables())
table=datastore.table(5249000000081181)
#table.delete_row(5249000000017011)
# column_data=table.get_column_details(5249000000032372)
# print(column_data)

# columns=table.get_all_columns()
# print(columns)
# row = table.get_row(5249000000032385)
# print(row)

# next_token = None
# more_records=True
# while more_records:
#     row=table.get_paged_rows(next_token,max_rows=1)
#     print(row)
#     more_records=row['more_records']
#     if not more_records:
#         break
#     next_token=row['next_token']

# def getMyPagedRows(next_token = None,more_records = True) :
    
#     rows=table.get_paged_rows(next_token,max_rows=1)
#     print(rows)
#     more_records=rows['more_records']
#     if not more_records:
#         return None
#     next_token=rows['next_token']
#     return getMyPagedRows( next_token,more_records)
# getMyPagedRows()

"""row_data =[{'name': 'abc',  'id': '1222', 'age': '11'},{'name': 'abc',  'id': '1223', 'age': '10'}]
row_response=table.insert_rows(row_data)
print(row_response)"""

"""row_data =[{'name': 'abc',  'id': '1222', 'age': '21','ROWID': 5249000000032461},{'name': 'xyz',  'id': '100', 'age': '21','ROWID': 5249000000032459}]
row_response=table.update_rows(row_data)
print(row_response)"""
"""row_response=table.delete_rows([5249000000032405,5249000000032408,5249000000032411])
print(row_response)"""
#print(zcql.execute_query("SELECT COUNT(ROWID) FROM TodoItems")[0]['TodoItems']['ROWID'])
"""page=0
perpage=10
toda_items=[]
row_datas=zcql.instance().execute_query(f'SELECT ROWID,Notes FROM TodoItems LIMIT {page},{perpage}')
#print(row_datas)

for row_data in row_datas:
    data=dict({"id":"","notes":""})
    #print(row_data)
    data['id']= row_data['TodoItems']['ROWID']
    data['notes']=row_data['TodoItems']['Notes']
    #print(data)
    toda_items.append(data)
    print(toda_items)
print(toda_items)
response_data={}
response_data["status"]="success"
response_data["todoItems"]=toda_items
print(response_data)"""
# data={'notes': 'testq'}
# insert_response=table.insert_row({"Notes":data['notes']})
# table.delete_row(5249000000081908)
# print(insert_response['ROWID'])
# todo_dict={"todoItem": {"id": insert_response['ROWID'], "notes":data['notes']}}
# response_data={}
# response_data["status"]="success"
# response_data["data"]=todo_dict
# print(response_data)
# table.delete_row()
print(table.get_row(5249000000081908))
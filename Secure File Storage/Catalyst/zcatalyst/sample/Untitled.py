import json
import os
from typing import Dict, TypedDict
import zcatalyst
from zcatalyst import mail,cache,functions,datastore,filestore, zcql, user_management, cron, zia,search
from zcatalyst import connection
from zcatalyst import push_notification
from zcatalyst.cron import ICatalystCronUpdateReq, ICatalystCronReq
from zcatalyst.credentials import CookieCredential
from zcatalyst.catalyst_app import CatalystApp
import threading

# Note - provide credentials in env or inline
os.environ['CATALYST_AUTH'] = json.dumps({'refresh_token':'1000.3b7ea5fcd8398f9d9171794cad9f00ac.807d50e0876a54059243a38b897a2180',
                                          'client_id':'1000.HN38DZYCSYQ8TU588BQ97RW44GSAMK',
                                          'client_secret':'4740ebde1bdcb3d7c3d14193fcdffe8a9f7864196c'})
os.environ['CATALYST_OPTIONS'] = json.dumps({'project_id':'5249000000008013','project_key':'1008807534','project_domain':'https://sample-71779596.development.localcatalystserverless.com'})
#------------------------------------------------------------------



app = zcatalyst.initialize_app()

# pn = push_notification.instance()
# aa = pn.web().send_notification("hii",["hariprabhu2323@gmail.com"])
# print(aa)

"""
# #---------------------------------------------------------------------------#
# '''MAIL'''
file1 = open('wallpaper.jpg','rb')
mail_obj = {
    'from_email': 'mahesh.annamalai@zohotest.com',
    'to_email': ['mahesh.annamalai+us@zohotest.com'],
	'subject': 'empty string',
    'display_name':'ZZZ',
    'attachments':[file1]
}

mail = mail.instance()
resp = mail.send_mail(mail_obj)
print(json.dumps(resp,indent=3))



# #----------------------------------------------------------------------------#
'''CACHE'''
cache = cache.instance()
all_segment_details = cache.get_all_segment()
for i in range(1,len(all_segment_details)+1):
    print(f'Segment {i} id = ' + str(all_segment_details[i-1]._id))
segment_id=5249000000008067
print(cache.get_segment_details(segment_id))
'''default cache operations'''
def_seg = cache.segment()
a= def_seg.put('hi','bye',1)
print(def_seg.get('hi'))
print(def_seg.get_value('hi'))
def_seg.update('hi','updated')
print(def_seg.get_value('hi'))

'''specific segment operations'''
s1 = cache.segment(segment_id)
s1.put('hi','bye')
print(s1.get('hi'))
print(s1.get_value('hi'))
s1.update('hi','updated')
print(s1.get_value('hi'))
print(s1.to_dict())
print(s1.to_string())
s1.delete("hi")


# #----------------------------------------------------------------------------#
'''Functions'''
fun = functions.instance()
resp = fun.execute(5249000000015567)
print(resp)



# #----------------------------------------------------------------------------#
# '''DataStore'''

db = datastore.instance()
table1 = db.get_all_tables()[0]
print(table1.to_dict())


# resp = table1.insert_rows(
#     [
#         {
#             'name':'ARAVIND',
#             'age':26
#         }
#     ]
# )
# print(resp)

for row in table1.get_iterable_rows():
    print(row)




# #----------------------------------------------------------------------------#
# '''FileStore'''


fs = filestore.instance()
F1 = fs.get_folder_details(5249000000016011)
F1.upload_file({
    'code':open('/Users/hari-pt6161/Python/sample/scopes.txt','rb'),
    'name':'neww'
})
print('uploaded')

print("downloaded ---> " + str(F1.download_file(5249000000032058)))

raw_content = F1.get_file_stream(5249000000032058)
print(type(raw_content))
for i in raw_content.stream(1):
    print(i)
file_details=F1.get_file_details(5249000000032058)
print(file_details)

F1.update({'folder_name': "test01"})
F1.delete_file(5249000000112207)
F1.delete()


# #----------------------------------------------------------------------------#
'''User Management'''

um = user_management.instance(app)
# for i in um.get_all_users():
#     print(i)

signup_config = {
    'platform_type':"web",
    'zaid':'1008807534'
}

user_details = {
    'last_name':'Mahesh',
    'email_id':'200155mahesh@gmail.com',
    'zaaid':'1009184048'
}

# um.reset_password(signup_config,user_details)
# um.add_user_to_org(signup_config,user_details)
# print(um.get_current_user())
# print(um.delete_user(5249000000120655))
# um.register_user(signup_config,user_details)


# #----------------------------------------------------------------------------#
'''ZCQL'''
zqls = zcql.instance()
op1 = zqls.execute_query(f"SELECT ROWID,Notes FROM TodoItems LIMIT 0,100")

op = zqls.execute_query(f"SELECT ROWID,Notes FROM TodoItems LIMIT 0,100")
print(op[0].get('TodoItems').get('ROWID'))
todo_items= {}
for row in op:
    todo_items['id']=row['TodoItems']['ROWID']
    todo_items['notes']=row['TodoItems']['Notes']
print(todo_items)
print(zqls.get_component_name())

cr = cron.instance()
a = cr.get_all_cron()
for i in a:
    print(i['cron_name'])

app1 = zcatalyst.get_app()

print(app1.name)


# # ----------------------------------------------------------------------------#
'''connectors'''

prop = {
   'C1': {
    'refresh_token':'1000.d485269d59cd899c1157e04e4a534f29.81fb71a49ddcf731ae8ec00deae45e3f',
    'client_id':'1000.CA69IM419TWYBLMVWQ7BSO9HPT4VTF',
    'client_secret':'8934558be5250f3981fe6c5778b1b5c616e5fba9ed',
    'auth_url': 'https://accounts.localzoho.com/oauth/v2/auth',
    'refresh_url': 'https://accounts.localzoho.com/oauth/v2/token',
    }
}
ction = connection.instance(prop)
ctor = ction.get_connector('C1')
print(ctor.get_access_token())

#----------------------------------------------------------------------------#
'''zia'''
ziaService = zia.instance()
img = open('dog.jpg','rb')
resp = ziaService.detect_object(img)
print(resp)

img2 = open('dog.jpg','rb')
resp2 = ziaService.extract_optical_characters(img2,{'language':'tam'})
print(resp2)

ds = datastore.instance()
ds.table('TodoItems').insert_row({"Notes":"okok"})
#----------------------------------------------------------------------------#
'''search'''
search=search.instance()
config = {
        "search": 'ab*',
        "search_table_columns": {
            "test": ["notes"]
        }
    }
print(search.execute_search_query(config))"""
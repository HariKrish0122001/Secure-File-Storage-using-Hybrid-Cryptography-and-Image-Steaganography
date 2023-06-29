import zcatalyst
from zcatalyst import datastore,filestore,user_management
import os
import json
from io import BytesIO
import PIL.Image as Image
import base64
import io
import requests
# https://console.catalyst.localzoho.com/baas/71779596/project/5249000000687067/Development#/cloudscale/datastore/5249000000687108/schema

os.environ['CATALYST_AUTH'] = json.dumps(
    {'refresh_token': '1000.0e2f9bdcf8f047882cad13bdb99f4a49.c70f107fc82f39ec6dcbda5a65fca219',
     'client_id': '1000.HN38DZYCSYQ8TU588BQ97RW44GSAMK',
     'client_secret': '4740ebde1bdcb3d7c3d14193fcdffe8a9f7864196c'})
os.environ['CATALYST_OPTIONS'] = json.dumps({'project_id': '5249000000687067', 'project_key': 'projectkey',
                                             'project_domain': 'https://hybridcloud-71779596.development.localcatalystserverless.com'})

app=zcatalyst.initialize_app()
filestore_service=filestore.instance()
datastore_service= datastore.instance()
# print(datastore_service.get_all_tables())

folder_instance=filestore_service.folder(5249000000698001)



# file upload
path='/Users/hari-pt6161/Final yr /sfs/Secure-File-Storage-On-Cloud-Using-Hybrid-Cryptography/Final Yr/Catalyst/login.py'
fbuf=None
name=path.split('/')[-1]
with open(path, 'rb') as f:
    fbuf = io.BufferedReader(f)  
    data={
        'name':name, #path.split('/')[-1]
        "code":fbuf
    }
    response=folder_instance.upload_file(data)
    print(response)
    file_id=response['id']
    uploaded_by='hp@gamil.com'
    accessible_by='[hp321@gamil.com,hp123@gamil.com]'
    response_data={
        "File_id":file_id,
        "Name":name,
        "Uploaded_By":'hp@gamil.com' ,  #login cache
        "Accessible_by":accessible_by
    }
    response=datastore_service.get_table_details("FileDetails").insert_row(response_data)
    print(response)

# download a file 
some_bytes = filestore_service.folder("5249000000698001").download_file(5249000000705340)
binary_file = open('image.jpeg', "wb")
binary_file.write(some_bytes)
binary_file.close()

#list of file for user
user_id='hp@gmail.com'
file_list=[]
file_data=datastore_service.table(5249000001008401).get_paged_rows()['data']
for i in file_data:
    mylist=(i['Accessible_by'][1:-1]).split(',')
    if user_id in mylist:
        # print("true",mylist)
        dict1={"name":i['Name'],
               'id':i['File_id']}
        file_list.append(dict1)    
print(file_list)

#list of user
user_list=[]
user_data=datastore_service.table(5249000000687108).get_paged_rows()['data']
for i in user_data:
    user_list.append(i['Mail_id'])
print(user_list)
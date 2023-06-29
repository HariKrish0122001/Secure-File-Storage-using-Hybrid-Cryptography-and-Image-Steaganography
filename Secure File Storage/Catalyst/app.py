import os

os.environ['X_ZOHO_CATALYST_CONSOLE_URL'] = "https://console.catalyst.zoho.in"
os.environ['X_ZOHO_CATALYST_ACCOUNTS_URL'] = 'https://accounts.zoho.in'

import shutil
import zcatalyst
from zcatalyst import datastore, filestore, user_management
import json
from io import BytesIO
import PIL.Image as Image
import io

import sys
sys.path.append('../')
import enc
import dec
# https://console.catalyst.localzoho.com/baas/71779596/project/5249000000687067/Development#/cloudscale/datastore/5249000000687108/schema


os.environ['CATALYST_AUTH'] = json.dumps(
    {'refresh_token': '',
     'client_id': '',
     'client_secret': ''})
os.environ['CATALYST_OPTIONS'] = json.dumps({'project_id': '', 'project_key': '',
                                             'project_domain': ''})

app = zcatalyst.initialize_app()
filestore_service = filestore.instance()
datastore_service = datastore.instance()
print(datastore_service.get_all_tables())

folder_instance = filestore_service.folder(25000000005490)





def downloadFile(data):
    key = data['key']
    file_id = data['id']  # "5249000001184041"  # '123'
    user_details = datastore_service.get_table_details("FileDetails").get_paged_rows()['data']
    # print(user_details)
    for i in user_details:
        if (i["Key_Value"] == key and i['File_id'] == file_id):
            cur_path = os.getcwd()
            path = os.path.join(cur_path, 'Download/files')
            some_bytes = filestore_service.folder("25000000005490").download_file(data['id'])
            binary_file = open(os.path.join(path, data['file_name']), "wb")
            binary_file.write(some_bytes)
            binary_file.close()
            return True


    else:
        print("Invalid details")
        return False


def uploadFile(file_details,cookie):
    cur_path = os.getcwd()
    # parent_path=os.path.abspath(os.path.join(cur_path, os.pardir))

    path = os.path.join(cur_path, 'uploads/files', file_details['file_name'])
    print("path---", path)
    # path='/Users/hari-pt6161/Final yr /sfs/Secure-File-Storage-On-Cloud-Using-Hybrid-Cryptography/Final Yr/Catalyst/login.py'
    fbuf = None
    name = path.split('/')[-1]
    with open(path, 'rb') as f:
        fbuf = io.BufferedReader(f)
        data = {
            'name': name,  # path.split('/')[-1]
            "code": fbuf
        }
        response = folder_instance.upload_file(data)
        print(response)
        file_id = response['id']
        data = dec.decrypt_aes(cookie, "0123456789ABCDEF")

        uploaded_by = data.split(" : ")[0]
        accessible_by = file_details['receivers']  # '[hp321@gamil.com,hp123@gamil.com]'
        key = file_details['key']
        response_data = {
            "File_id": file_id,
            "Name": name,
            "Uploaded_By": uploaded_by,  # login cache
            "Accessible_by": accessible_by,
            "Key_Value": key
        }
        response = datastore_service.get_table_details("FileDetails").insert_row(response_data)
        print(response)
        return True


def loginCheck(data):
    mail_id = data['Mail_id']  # 'hp@gmail.com'
    password = data['Password']  # '123'
    user_details = datastore_service.get_table_details("UserDetails").get_paged_rows()['data']
    # print(user_details)
    for i in user_details:
        if (i["Mail_id"] == mail_id and i['Password'] == password):
            print("success")
            return True
    else:
        print("Invalid details")
        return False


def Signup(data):
    mail_id = data['Mail_id']  # 'hp123@gmail.com'
    password = data['Password']  # '123'
    user_id = '1'
    name = data['Name']  # 'hari'

    data = {'Mail_id': mail_id, 'User_id': user_id, 'Name': name, 'Password': password}
    user_list = Userlist()['user']

    for i in user_list:
        if(i == mail_id):
            return False
    else:
        response = datastore_service.get_table_details("UserDetails").insert_row(data)
        print(response)
        return True


def Userlist():
    user_list = []
    user_data = datastore_service.table(25000000004001).get_paged_rows()['data']
    for i in user_data:
        user_list.append(i['Mail_id'])
    print(user_list)
    return {"user": user_list}


def FileList(cookie):
    data = dec.decrypt_aes(cookie, "0123456789ABCDEF")
    user_id = data.split(" : ")[0] #'hariprabhu2323@gmail.com'
    file_list = []
    file_data = datastore_service.table(25000000004743).get_paged_rows()['data']
    for i in file_data:
        mylist = (i['Accessible_by'][1:-1]).split(',')
        # print(i['Accessible_by'])
        if user_id in mylist:
            # print("true",mylist)
            dict1 = {"name": i['Name'],
                     'id': i['File_id']}

            file_list.append(dict1)
    return file_list


def clearFolders(path):
    folder = path
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def setCookie(mail_id, password):
    return enc.encrypt_aes(mail_id + " : " + password, "0123456789ABCDEF")


def checkAuth(cookie):
    data = dec.decrypt_aes(cookie, "0123456789ABCDEF")
    mail_id = data.split(" : ")[0]
    password = data.split(" : ")[1]
    if (loginCheck({"Mail_id": mail_id, "Password": password})):
        return True
    else:
        return False

def renaming_format(path):
    path2=path.split('.')[0]+'.png'
    print(path2)
    os.rename(path, path2)

cookie ="TTitKLaO633vxPP4wp+OeeAiu8EZVrG/2mDHJuEDx6OdLNqQG2gtM1lwmlqyQZYk"
data = dec.decrypt_aes(cookie, "0123456789ABCDEF")
mail_id = data.split(" : ")[0]
print(mail_id)



#
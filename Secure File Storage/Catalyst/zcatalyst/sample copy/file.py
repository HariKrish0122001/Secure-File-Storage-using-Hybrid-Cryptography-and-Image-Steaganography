import zcatalyst
from zcatalyst import filestore
import os
import json
import io

os.environ['CATALYST_AUTH'] = json.dumps({'refresh_token':'1000.870a8432310cf16fb3e41e21ee7ea032.fce64c75a58b646e20d7574dbc95d792',
                                          'client_id':'1000.HN38DZYCSYQ8TU588BQ97RW44GSAMK',
                                          'client_secret':'4740ebde1bdcb3d7c3d14193fcdffe8a9f7864196c'})
os.environ['CATALYST_OPTIONS'] = json.dumps({'project_id':'5249000000008013','project_key':'1008807534','project_domain':'https://sample-71779596.development.localcatalystserverless.com'})

zcatalyst.initialize_app()
filestore=filestore.instance()
folder=filestore.folder(5249000000016011)
#filestore.create_folder("Test_to_create")
#file=filestore.folder("5249000000015501").download_file("5249000000015547")
#print(type(file))
#print(file)
#file1=filestore.create_folder("HP1")
#print(file1)
"""file21=filestore.create_folder("Test3")
print(file21)"""
#filestore.folder("5249000000015524").delete()
#print(filestore.get_all_folders())
path='/Users/hari-pt6161/Python/sample/tab.py'
fbuf=None
f = open('/Users/hari-pt6161/Python/sample/tab.py', "rb")
"""with open(path, 'rb') as _file:
    fbuf = io.BufferedReader(_file)"""
#print(f)
#folder.upload_file({'code':f,'name':'ABC1.txt'})
"""with open(path, 'rb') as f:
    folder.upload_file({'code':f,'name':'ABC.txt'})"""
"""config = {
        'code': open('/Users/hari-pt6161/Python/sample/tab.py', "rb"),
        'name': 'testFile.txt'
}
folder.upload_file(config)"""
# data=folder.delete_file(5249000000032063)
# print(data)
print(type(folder.download_file(5249000000112184)))
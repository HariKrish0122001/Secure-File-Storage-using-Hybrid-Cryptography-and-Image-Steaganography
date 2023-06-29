import json
import os,io
from zcatalyst import filestore,functions
import zcatalyst

os.environ['CATALYST_AUTH'] = json.dumps(
    {'refresh_token': '1000.0e2f9bdcf8f047882cad13bdb99f4a49.c70f107fc82f39ec6dcbda5a65fca219',
     'client_id': '1000.HN38DZYCSYQ8TU588BQ97RW44GSAMK',
     'client_secret': '4740ebde1bdcb3d7c3d14193fcdffe8a9f7864196c'})
os.environ['CATALYST_OPTIONS'] = json.dumps({'project_id': '5249000000008013', 'project_key': '1008807534',
                                             'project_domain': 'https://sample-71779596.development.localcatalystserverless.com'})

zcatalyst.initialize_app()
filestore=filestore.instance()
# all_folder=filestore.get_all_folders()

# folder_id=5249000000191039
# file_id=5249000000191056
# print(type(all_folder))
# folder=all_folder[0]
# print(type(folder))
# print(folder.get_file_details())
# # print(folder.to_dict())
# path =  "/Users/hari-pt6161/Python/data/img1.jpeg"
# path2 =  "/Users/hari-pt6161/Python/data/img2.png"
# file1, file2 = None, None
# with open(path, 'rb') as _file:
#     file1 = io.BufferedReader(_file)
#     file_details={"code": file1,
#                 "name": "test"
#     }
#     # print(folder.upload_file(file_details)['file_name']=="test")
# with open(path2, 'rb') as _file:
#     file2 = io.BufferedReader(_file)
#     file_details={"code": file2,
#                 "name": "test"
#     }
#     print(folder.update({"folder_name": "new"})['folder_name']=="new")
# # file_id=
# print(folder.get_file_stream())
# test_folder=filestore.create_folder("test")
# print(type(test_folder))
# test_folder_id=test_folder._id
# test_folder=filestore.folder(test_folder_id)

# print(type(filestore.get_folder_details(test_folder_id)))
# print("____________________")
# print(type(filestore.get_all_folders()[0]._id))
# print(test_folder.delete())

# file1, file2 = None, None
# with open("/Users/hari-pt6161/Python/data/img2.png", 'rb') as _file:
#     file1 = io.BufferedReader(_file)
#     config = {
#         'code': file1,
#         'name': 'testFile.txt'
# }
#     response=test_folder.upload_file(config)
#     print(response['file_name'])
# file_id=response['id']
# # print(type(test_folder.download_file(file_id)))
# # print(test_folder.get_file_details(file_id))
# # print(type(test_folder.get_file_stream(file_id)))
# # print(test_folder.update({'folder_name': "test2"}))
# print(test_folder._folder_details)
# print(test_folder.delete_file(file_id))
# print(test_folder.delete())
functions=functions.instance()
function_id="5249000000015567"
print(functions.execute(function_id))
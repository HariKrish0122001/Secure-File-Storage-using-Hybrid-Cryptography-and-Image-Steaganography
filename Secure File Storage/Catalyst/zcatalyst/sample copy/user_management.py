import zcatalyst
from zcatalyst import zcql,mail,user_management
import os
import json
import io,sys

os.environ['CATALYST_AUTH'] = json.dumps({'refresh_token':'1000.3b7ea5fcd8398f9d9171794cad9f00ac.807d50e0876a54059243a38b897a2180',
                                          'client_id':'1000.HN38DZYCSYQ8TU588BQ97RW44GSAMK',
                                          'client_secret':'4740ebde1bdcb3d7c3d14193fcdffe8a9f7864196c'})
os.environ['CATALYST_OPTIONS'] = json.dumps({'project_id':'5249000000008013','project_key':'1008807534','project_domain':'https://sample-71779596.development.localcatalystserverless.com'})

zcatalyst.initialize_app()
um = user_management.instance()
# for i in um.get_all_users():
#     print(i)

signup_config = {
    'platform_type':"web",
    'zaid':'1008807534'
}

user_details = {
    # 'first_name': "Hariprabhu123800",
    # 'last_name':'HP812390',
    'email_id':'hari0888000@gmail.com',
    #'role_id':'5249000000008026'#'3376000000159024'#1009184048
}
print(um.add_user_to_org(signup_config=signup_config,user_details=user_details))
# print(um.get_current_user())#error
# print(um.get_user_details(5249000000215001))  
# print(um.get_all_users())
# print(um.register_user(signup_config,user_details))
# print(um.reset_password(signup_config,user_details))#error
# print(um.delete_user(5249000000213045))
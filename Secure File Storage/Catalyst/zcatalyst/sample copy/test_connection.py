from unittest.mock import ANY
import zcatalyst
from zcatalyst import cron
from zcatalyst import connection
from zcatalyst.connection import Connector
import os
import responses
import json

os.environ['CATALYST_AUTH'] = json.dumps({'refresh_token':'1000.c246243bdd0b7ca2b949e2c43851f414.1124d93af995931d81baa62801d0ed7d',
                                          'client_id':'1000.HN38DZYCSYQ8TU588BQ97RW44GSAMK',
                                          'client_secret':'4740ebde1bdcb3d7c3d14193fcdffe8a9f7864196c'})
os.environ['CATALYST_OPTIONS'] = json.dumps({'project_id':'5249000000008013','project_key':'1008807534','project_domain':'https://sample-71779596.development.localcatalystserverless.com'})

zcatalyst.initialize_app()
connection=connection.instance({
 'ConnectorName': {
   'client_id':'1000.HN38DZYCSYQ8TU588BQ97RW44GSAMK',
   'client_secret':'4740ebde1bdcb3d7c3d14193fcdffe8a9f7864196c',
   'auth_url': 'https://accounts.localzoho.com/oauth/v2/token?',
   'refresh_url': 'https://accounts.localzoho.com/oauth/v2/token?',
   'refresh_token': '1000.2269c5fc1fb7a83374c020988f03db2f.1939bb136e7ae87b12a5e56af8776d22'
  }
 })

connector_name="ABC"
connector_details={'client_id': '1000.HN38DZYCSYQ8TU588BQ97RW44GSAMK', 
                    'client_secret': '4740ebde1bdcb3d7c3d14193fcdffe8a9f7864196c', 
                    'auth_url': 'https://accounts.localzoho.com/oauth/v2/token?', 
                    'refresh_url': 'https://accounts.localzoho.com/oauth/v2/token?', 
                    'refresh_token': '1000.2269c5fc1fb7a83374c020988f03db2f.1939bb136e7ae87b12a5e56af8776d22',
                    'connector_name':connector_name,
                    'redirect_url':"https://sample-71779596.development.localcatalystserverless.com"}
#print(connection.__dict__)
# print(connection.get_connector(connector_name="{'client_id': '1000.HN38DZYCSYQ8TU588BQ97RW44GSAMK', 'client_secret': '4740ebde1bdcb3d7c3d14193fcdffe8a9f7864196c', 'auth_url': 'https://sample-71779596.development.localcatalystserverless.com', 'refresh_url': 'https://sample-71779596.development.localcatalystserverless.com', 'refresh_token': '1000.c246243bdd0b7ca2b949e2c43851f414.1124d93af995931d81baa62801d0ed7d'}"))
print(type(connection.get_connector('ConnectorName')))
#print(connection._get_connection_json({'client_id': '1000.HN38DZYCSYQ8TU588BQ97RW44GSAMK', 'client_secret': '4740ebde1bdcb3d7c3d14193fcdffe8a9f7864196c', 'auth_url': 'https://sample-71779596.development.localcatalystserverless.com', 'refresh_url': 'https://sample-71779596.development.localcatalystserverless.com', 'refresh_token': '1000.c246243bdd0b7ca2b949e2c43851f414.1124d93af995931d81baa62801d0ed7d'}))
connector=Connector(connection_instance=connection,connector_details=connector_details)
# print(connector.generate_access_token("1000.a8f67708e757248638f69aa89a684cac.de7031893119a49616c09bfcb769194c"))
# print(connector.get_access_token())


# print(connector.generate_access_token(code="1000.fe6137b0ce8c8d080d02a0f18d55e8a8.4b84764590d24636aa1cbf71dfe557ad"))
# @responses.activate
# def test_get_access_token():

#     responses.get(
#         responses.GET,
#         ' https://console.catalyst.localzoho.com/baas/v1/project/5249000000008013/cache?cacheKey=ZC_CONN_ABC',
#         json={
#             'data': [
#                 {
#                     'segment_name': 'Default',
#                     'project_details': {
#                         'project_name': 12345,
#                         'id': 123
#                     },
#                     'id': 123
#                 }
#             ]
#         },
#         status='success'
#     )
#     print(connector.get_access_token())
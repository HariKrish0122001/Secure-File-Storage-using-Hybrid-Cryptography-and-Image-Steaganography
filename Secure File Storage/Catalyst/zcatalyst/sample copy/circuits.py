import zcatalyst
from zcatalyst import zcql,mail,user_management,circuit
import os
import json
import io,sys

os.environ['CATALYST_AUTH'] = json.dumps({'refresh_token':'1000.962c9402fc5a9b10cebc7c570ffe6f26.67312aa0a9361ce9e2fd36681fcaaa45',
                                          'client_id':'1000.HN38DZYCSYQ8TU588BQ97RW44GSAMK',
                                          'client_secret':'4740ebde1bdcb3d7c3d14193fcdffe8a9f7864196c'})
os.environ['CATALYST_OPTIONS'] = json.dumps({'project_id':'5249000000008013','project_key':'1008807534','project_domain':'https://sample-71779596.development.localcatalystserverless.com'})

zcatalyst.initialize_app()
circuit_service=circuit.instance()
# print(circuit_service.execute(5249000000108030,name="test123"))
# print(circuit_service.get_component_name())
# print(circuit_service.status(circuit_id=5249000000108030,exec_id="bf0c20ca-4e32-4bb0-b64a-8dd98a532532"))
# print(circuit_service.abort(circuit_id=5249000000108030,exec_id="bf0c20ca-4e32-4bb0-b64a-8dd98a532532"))
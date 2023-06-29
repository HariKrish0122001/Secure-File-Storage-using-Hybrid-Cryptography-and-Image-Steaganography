import zcatalyst
from zcatalyst import search,datastore
import os
import json
import io
import sys

os.environ['CATALYST_AUTH'] = json.dumps({'refresh_token':'1000.3b7ea5fcd8398f9d9171794cad9f00ac.807d50e0876a54059243a38b897a2180',
                                          'client_id':'1000.HN38DZYCSYQ8TU588BQ97RW44GSAMK',
                                          'client_secret':'4740ebde1bdcb3d7c3d14193fcdffe8a9f7864196c'})
os.environ['CATALYST_OPTIONS'] = json.dumps({'project_id':'5249000000008013','project_key':'1008807534','project_domain':'https://sample-71779596.development.localcatalystserverless.com'})

app=zcatalyst.initialize_app()
search=search.instance()
#print(search.get_component_name())
config = {
        "search": 'a*',
        "search_table_columns": {
            "test": ["notes"]
        }
    }
print(search.execute_search_query(config))
#print(datastore.instance().table(5249000000081181).get_all_columns())

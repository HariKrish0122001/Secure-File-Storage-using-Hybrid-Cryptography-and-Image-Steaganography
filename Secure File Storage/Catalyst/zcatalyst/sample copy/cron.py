import json
import os
from zcatalyst import cron
import zcatalyst

os.environ['CATALYST_AUTH'] = json.dumps(
    {'refresh_token': '1000.ebf13e2601c2fce1631fa41a075e2c6a.4675920ac533ea08a814a2890522e949',
     'client_id': '1000.HN38DZYCSYQ8TU588BQ97RW44GSAMK',
     'client_secret': '4740ebde1bdcb3d7c3d14193fcdffe8a9f7864196c'})
os.environ['CATALYST_OPTIONS'] = json.dumps({'project_id': '5249000000008013', 'project_key': '1008807534',
                                             'project_domain': 'https://sample-71779596.development.localcatalystserverless.com'})

zcatalyst.initialize_app()
cron=cron.instance()
# print(cron.create_cron(cron_details={"cron_name":"aa12",
#                             "description":"aa",
#                             "cron_type":"Periodic",
#                             #"cron_function_id":"5249000000022001",
#                             "cron_function_identifier":"newsfetch",
#                             "cron_url_details":{"url_id":"5249000000025860",#5249000000025860
#                             "url":"","headers":{},"params":{}},
#                             "status":'true',
#                             #"created_time":"Oct 14, 2022 03:45 PM",
#                             # "created_by":{"zuid":"71779587","is_confirmed":'false',"email_id":"hariprabhu.mj@zohotest.com","first_name":"Hariprabhu","last_name":"M","user_type":"Admin","user_id":"5249000000008003"},
#                             # "modified_time":"Oct 14, 2022 03:45 PM",
#                             # "modified_by":{"zuid":"71779587","is_confirmed":'false',"email_id":"hariprabhu.mj@zohotest.com","first_name":"Hariprabhu","last_name":"M","user_type":"Admin","user_id":"5249000000008003"},
#                             # "project_details":{"project_name":"Sample","id":"5249000000008013","project_type":"Live"},"end_time":"-1",
#                             "job_detail":{"jobId":"5249000000025863","transactionTimeout":-1,"hour":1,"minute":0,"second":0,"timezone":"America/Los_Angeles"}
#                             }))

# cron.delete_cron(5249000000025878)
# print((cron.get_all_cron()[0]))
# print(cron.get_cron_details(5249000000025863))
print(cron.update_cron( cron_details={
                            "id":"5249000000204134",
                            "cron_name":"aa122",
                            "description":"abc",
                            "cron_type":"Periodic",
                            "cron_function_identifier":"newsfetch",
                            "cron_url_details":{"url_id":"",
                            "url":"","headers":{},"params":{}},
                            "status":'true',
                            "job_detail":{"jobId":"5249000000025863","transactionTimeout":-1,
                            "hour":1,"minute":0,"second":0,"timezone":"America/Los_Angeles"}
                            }))
# print(cron.create_cron())

"""connection=connection.instance({
 ConnectorName: {
   client_id: '{client_id}',
   client_secret: '{client_secret}',
   auth_url: '{auth_url}',
   refresh_url: '{refresh_url}',
   refresh_token: '{refresh_token}'
  }
 })"""
# connection.get_connector("Abc")

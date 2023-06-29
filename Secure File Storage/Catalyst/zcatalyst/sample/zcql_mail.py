import zcatalyst
from zcatalyst import zcql,mail
import os
import json
import io,sys

os.environ['CATALYST_AUTH'] = json.dumps({'refresh_token':'1000.5134d22795deaefbe8d58ed1f8f5ba4f.2426363a3b260e204ea52054946b5cde',
                                          'client_id':'1000.HN38DZYCSYQ8TU588BQ97RW44GSAMK',
                                          'client_secret':'4740ebde1bdcb3d7c3d14193fcdffe8a9f7864196c'})
os.environ['CATALYST_OPTIONS'] = json.dumps({'project_id':'5249000000008013','project_key':'1008807534','project_domain':'https://sample-71779596.development.localcatalystserverless.com'})

zcatalyst.initialize_app()
zcql=zcql.instance()
# print(zcql.execute_query("SELECT * FROM TodoItems"))
# print(zcql.get_component_name())
fbuf=None
path="/Users/hari-pt6161/Python/sample/wallpaper.jpg"
with open(path,'rb')as _file:
    fbuf = io.BufferedReader(_file)
    #print(fbuf)
    attachment=[]
    attachment.append(fbuf)
    _MAIL_OBJ_DICT = {
    'from_email': 'hariprabhu.mj+test@zohotest.com',
    'to_email': ["hariprabhu.mj@zohocorp.com"],
    'cc':["hariprabhu2323@gmail.com"],
    'bcc':["ham.gunn@zylker.com","rover.jenkins@zylker.com"],
    'reply_to':["hariprabhu2323@gmail.com"],
    'subject': 'Greetings from Zylker Corp!',
    'attachments': [fbuf],
    'content': "<p>Hello,</p> We're glad to welcome you at Zylker Corp. To begin your journey with us, please download the attached KYC form and fill in your details. You can send us the completed form to this same email address.</p>We cannot wait to get started!<p><p>Cheers!</p><p>Team Zylker</p>"

}
    mail=mail.instance()
    print(mail._generate_data(_MAIL_OBJ_DICT))
    # print(mail.send_mail(_MAIL_OBJ_DICT))
# data=mail._generate_data(_MAIL_OBJ_DICT)
# print(data[-1][-1])
# print(zcql.get_component_name())
# print(zcql.execute_query("SELECT Names FROM Auth"))
# items=[]
# row_datas=zcql.execute_query("SELECT Names FROM Auth")
# print(row_datas)
# for row_data in row_datas:
#     data=dict({"Names":""})
#     #print(row_data)
#     data['Names']= row_data['Auth']['Names']
#     #print(data)
#     items.append(data)
# response = {"status": "success", "data": items}
# print(response)
# print(zcql.execute_query("SELECT notes FROM test"))
# response =[{'test': {'notes': 'abc'}}, {'test': {'notes': 'abcc'}}, {'test': {'notes': 'aaabc'}}]
# print("notes" in (response[0]["test"].keys()))
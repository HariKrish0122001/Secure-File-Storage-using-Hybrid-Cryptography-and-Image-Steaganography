import json
import os,io,sys
from zcatalyst import mail
import zcatalyst

os.environ['CATALYST_AUTH'] = json.dumps(
    {'refresh_token': '1000.0e2f9bdcf8f047882cad13bdb99f4a49.c70f107fc82f39ec6dcbda5a65fca219',
     'client_id': '1000.HN38DZYCSYQ8TU588BQ97RW44GSAMK',
     'client_secret': '4740ebde1bdcb3d7c3d14193fcdffe8a9f7864196c'})
os.environ['CATALYST_OPTIONS'] = json.dumps({'project_id': '5249000000008013', 'project_key': '1008807534',
                                             'project_domain': 'https://sample-71779596.development.localcatalystserverless.com'})

zcatalyst.initialize_app()
mail = mail.instance()
path="/Users/hari-pt6161/Python/data/img2.png"
fbuf=None
with open(path,'rb')as _file:
    fbuf = io.BufferedReader(_file)
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
    mail.send_mail(_MAIL_OBJ_DICT)
import zcatalyst
from zcatalyst import zia,circuit,functions
import os
import json
import io
import sys

os.environ['CATALYST_AUTH'] = json.dumps({'refresh_token':'1000.3b7ea5fcd8398f9d9171794cad9f00ac.807d50e0876a54059243a38b897a2180',
                                          'client_id':'1000.HN38DZYCSYQ8TU588BQ97RW44GSAMK',
                                          'client_secret':'4740ebde1bdcb3d7c3d14193fcdffe8a9f7864196c'})
os.environ['CATALYST_OPTIONS'] = json.dumps({'project_id':'5249000000008013','project_key':'1008807534','project_domain':'https://sample-71779596.development.localcatalystserverless.com'})

zcatalyst.initialize_app()
zia1=zia.instance()
path=os.path.join(sys.path[0])+"/wallpaper.jpg"
path=os.path.join(sys.path[0])+"/wallpaper.jpg"
# print(os.path.dirname(os.path.dirname(__file__))+"/wallpaper.jpg")
print(os.path.dirname(__file__))
# print(sys.path)
# fbuf2=None
# with open(path, 'rb') as _file:
#     with open(path,'rb')as _file2:
#         fbuf = io.BufferedReader(_file)
#         fbuf2 = io.BufferedReader(_file2)

        # print(zia1.moderate_image(fbuf2,options={'mode': 'moderate'}))
        # print(zia1.analyse_face(fbuf2,options={
        # 'mode': 'moderate',
        # 'emotion':True,
        # 'age': True,
        # 'gender': False
        #     }))#doubt
        # print(zia1.detect_object(fbuf2))
        # print(zia1.extract_aadhaar_characters(fbuf,fbuf,language='eng,tam')) #error
        # print(zia1.extract_optical_characters(fbuf,))#error
        #print(zia.get_component_name())
        # print(zia1.get_keyword_extraction(['Zoho Corporation, is an Indian multinational technology company that makes web-based business tools. It is best known for Zoho Office Suite. The company was founded by Sridhar Vembu and Tony Thomas and has a presence in seven locations with its global headquarters in Chennai, India, and corporate headquarters in Pleasanton, California.']))
        # print(zia1.get_NER_prediction(['Zoho Corporation, is an Indian multinational technology company that makes web-based business tools. It is best known for Zoho Office Suite. The company was founded by Sridhar Vembu and Tony Thomas and has a presence in seven locations with its global headquarters in Chennai, India, and corporate headquarters in Pleasanton, California.']))
        
        # print(zia1.get_sentiment_analysis(['Zoho Corporation, is an Indian multinational technology company that makes web-based business tools. It is best known for Zoho Office Suite. The company was founded by Sridhar Vembu and Tony Thomas and has a presence in seven locations with its global headquarters in Chennai, India, and corporate headquarters in Pleasanton, California.'],['zoho']))
        #error
        # print(zia1.scan_barcode(fbuf,options={'format': 'code39'}))
        # print(zia1.get_text_analytics(['Zoho Corporation, is an Indian multinational technology company that makes web-based business tools. It is best known for Zoho Office Suite. The company was founded by Sridhar Vembu and Tony Thomas and has a presence in seven locations with its global headquarters in Chennai, India, and corporate headquarters in Pleasanton, California.']))
        #error

        #print(zia1.get_sentiment_analysis(list_of_docs=['Zoho Corporation, is an Indian multinational technology company that makes web-based business tools. It is best known for Zoho Office Suite. The company was founded by Sridhar Vembu and Tony Thomas and has a presence in seven locations with its global headquarters in Chennai, India, and corporate headquarters in Pleasanton, California.'],keywords=['Zoho']))
        # print(zia1.get_text_analytics(list_of_docs=['Zoho Corporation, is an Indian multinational technology company that makes web-based business tools. It is best known for Zoho Office Suite. The company was founded by Sridhar Vembu and Tony Thomas and has a presence in seven locations with its global headquarters in Chennai, India, and corporate headquarters in Pleasanton, California.'],keywords= ['Zoho']))
        # print(zia1.compare_face(fbuf,fbuf2))
        # print(zia1.auto_ml(model_id= 5249000000214044))
        # print(zia1.analyse_face(fbuf))
        
#function

# functions=functions.instance()
# # print(functions.get_component_name())
# print(functions.execute(5249000000015567))
# print(fbuf)
# fbuf= io.open("/Users/hari-pt6161/Python/sample/wallpaper.jpg", "rb")
# print(type(fbuf))
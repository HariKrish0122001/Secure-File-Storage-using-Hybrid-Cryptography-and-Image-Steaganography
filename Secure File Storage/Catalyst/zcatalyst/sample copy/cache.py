import json
import os
from zcatalyst import cache
import zcatalyst
cache.Segment.put
os.environ['CATALYST_AUTH'] = json.dumps(
    {'refresh_token': '1000.0e2f9bdcf8f047882cad13bdb99f4a49.c70f107fc82f39ec6dcbda5a65fca219',
     'client_id': '1000.HN38DZYCSYQ8TU588BQ97RW44GSAMK',
     'client_secret': '4740ebde1bdcb3d7c3d14193fcdffe8a9f7864196c'})
os.environ['CATALYST_OPTIONS'] = json.dumps({'project_id': '5249000000008013', 'project_key': '1008807534',
                                             'project_domain': 'https://sample-71779596.development.localcatalystserverless.com'})

zcatalyst.initialize_app()
cache = cache.instance()
all_segment_details = cache.get_all_segment()
def_segment_details =all_segment_details[-1]
print(type(def_segment_details))
# def_segment_details.put("key","value")
# print(def_segment_details.get("key")['cache_value']=="value")
# print(def_segment_details.get_value("key")=="value")
# def_segment_details.update("key","value2")
# print(def_segment_details.get_value("key")=="value2")
# print(def_segment_details.delete("key"))
# print(type(def_segment_details.to_dict())==dict)
# print(type(def_segment_details.to_string())==str)
def_segment_id=def_segment_details._id
print(cache.get_segment_details(def_segment_id))
# print(def_segment_details.put("key","value"))
# print(def_segment_details.get("key")['cache_value']=)
print(cache.segment(52490000000080))











# print(all_segment_details)
# cache.segment(id="123")
"""for i in range(1,len(all_segment_details)+1):
    print(f'Segment {i} id = ' + str(all_segment_details[i-1]._id))

cache1=cache.get_segment_details("5249000000008067")
print(cache1)"""
'''default cache operations
def_seg = cache.segment()
a= def_seg.put('hi hp','bye',1)
print(def_seg.get('hi'))
print(def_seg.get_value('hi'))
def_seg.update('hi','updated hpp')
print(def_seg.get_value('hi'))'''

'''specific segment operations
s1 = cache.segment(5249000000008067)
s1.put('hi','bye1')
print(s1.get('hi'))
print(s1.get_value('hi'))
s1.update('hi','updated1')
print(s1.get_value('hi'))'''
# cache.segment().update("5249000000011016","")
"""s2 = cache.segment().update("888","1234")
s3= cache.segment(5249000000008067)
#s2.put('hi2','bye from ')
for i in range(1000):
    s3.put(f"{i}",f"{i}hello")
"""
# segment = cache.segment()
# # segment.put("key",'value')
# segment.update("data", "new val")
# segment.delete('data')
# print(segment.get('data'))

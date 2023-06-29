class MyClass:
    def __init__():
        pass
    
    def get_partition_values(self) :
        
        s1=self.data()

        return s1
    def data():
        return 10

# @patch("zcatalyst._http_client.HttpClient.request")
#     def test_generate_access_token(self,mock_req):
#         with patch('zcatalyst.connection._connector.cache.Segment.put') as mocked_data:
            
#             #mocked_boto3.return_value.list_objects_v2.return_value = object_result_di
#             mocked_data.return_value={'cache_value':{}}
#             mock_resp = MagicMock()
#             mock_resp.response_json = {'access_token': '1000.9056053d2e0d40a2518bb5f947ea8e81.4053562fe413c62d3a1fbfabce25fad6', 
#                                     'api_domain': 'https://api.localzoho.com', 
#                                     'token_type': 'Bearer', 
#                                     'expires_in': 3600}
#             mock_req.return_value = mock_resp
#             with patch('zcatalyst.connection._connector.cache.Segment.get') as mocked_data1:
#                 mocked_data1.return_value={'cache_value':{}}

#                 assess_token = self.connector.get_access_token()
#                 assert isinstance(assess_token,str)
#                 print(assess_token)


from __future__ import nested_scopes
import nested
import pytest
import responses
from unittest.mock import patch

class TestNested:
    def test_data(self):
        with patch.object(nested.MyClass,'data',return_value=5) as mocked_data:
            
            d1=nested.MyClass.get_partition_values(nested.MyClass)
            print("-------",d1)
            assert d1==5


#print(nested.MyClass.get_partition_values(nested.MyClass))

@responses.activate
def test_get_access_token(self):

    responses.add(
        responses.GET,
        ' https://console.catalyst.localzoho.com/baas/v1/project/12345/cache?cacheKey=ZC_CONN_ABC',
        json={
            'data': [
                {
                    'segment_name': 'Default',
                    'project_details': {
                        'project_name': project_id,
                        'id': project_id
                    },
                    'id': segment_id
                }
            ]
        },
        status='success'
    )
    
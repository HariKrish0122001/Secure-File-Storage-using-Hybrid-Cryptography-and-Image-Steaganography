from typing import Dict, Optional
from zcatalyst.types import (
    ICatalystCache,
    ICatalystProject,
    ICatalystSegment,
    ParsableComponent
)
from zcatalyst.exceptions import CatalystCacheError
from .._constants import (
    RequestMethod,
    CredentialUser,
    Components
)


class ICatalystCacheResp(ICatalystCache):
    project_details: Optional[ICatalystProject]


class Segment(ParsableComponent):
    def __init__(self, cache_instance, segment_details: Dict):
        if segment_details and not isinstance(segment_details, dict):
            raise CatalystCacheError(
                'INVALID_SEGMENT_DETAILS',
                'Segment details must be a non empty dict'
            )
        self._requester = cache_instance._requester
        self._id = segment_details.get('id') if segment_details else None
        self._segment_name = segment_details.get('segment_name') if segment_details else None

    def __repr__(self) -> str:
        return str(self.to_dict())

    def get_component_name(self):
        return Components.CACHE

    def put(
            self,
            key: str,
            value: str,
            expiry: int = None
    ) -> ICatalystCacheResp:
        if not key or not isinstance(key, str):
            raise CatalystCacheError(
                'INVALID_CAHCE_KEY',
                'Cache key must be a non empty string.'
            )
        api_path = f'/segment/{self._id}/cache' if self._id else '/cache'
        req_json = {
            'cache_name': key,
            'cache_value': value,
            'expiry_in_hours': expiry
        }
        resp = self._requester.request(
            method=RequestMethod.POST,
            path=api_path,
            json=req_json,
            user=CredentialUser.ADMIN
        )
        resp_json = resp.response_json
        return resp_json.get('data')

    def update(
            self,
            key: str,
            value: str,
            expiry: int = None
    ) -> ICatalystCacheResp:
        if not key or not isinstance(key, str):
            raise CatalystCacheError(
                'INVALID_CACHE_KEY',
                'Cache key must be a non empty string.'
            )
        api_path = f'/segment/{self._id}/cache' if self._id else '/cache'
        req_json = {
            'cache_name': key,
            'cache_value': value,
            'expiry_in_hours': expiry
        }
        resp = self._requester.request(
            method=RequestMethod.PUT,
            path=api_path,
            json=req_json,
            user=CredentialUser.ADMIN
        )
        resp_json = resp.response_json
        return resp_json.get('data')

    def get(
            self,
            key: str
    ) -> ICatalystCacheResp:
        if not key or not isinstance(key, str):
            raise CatalystCacheError(
                'INVALID_CACHE_KEY',
                'Cache key must be a non empty string.'
            )
        api_path = f'/segment/{self._id}/cache' if self._id else '/cache'
        query_params = {
            'cacheKey': key
        }
        resp = self._requester.request(
            method=RequestMethod.GET,
            path=api_path,
            params=query_params,
            user=CredentialUser.ADMIN
        )
        resp_json = resp.response_json
        return resp_json.get('data')

    def get_value(self, key: str) -> str:
        cache_obj = self.get(key)
        return cache_obj.get('cache_value')

    def delete(self, key: str) -> bool:
        if not key or not isinstance(key, str):
            raise CatalystCacheError(
                'INVALID_CACHE_KEY',
                'Cache key must be a non empty string.'
            )
        api_path = f'/segment/{self._id}/cache' if self._id else '/cache'
        query_params = {
            'cacheKey': key
        }
        resp = self._requester.request(
            method=RequestMethod.DELETE,
            path=api_path,
            params=query_params,
            user=CredentialUser.ADMIN
        )
        return bool(resp)

    def to_dict(self) -> ICatalystSegment:
        return {
            'id': self._id,
            'segment_name': self._segment_name
        }

    def to_string(self):
        return repr(self)

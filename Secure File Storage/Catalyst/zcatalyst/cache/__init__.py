from typing import List, Union
from zcatalyst.types import Component
from zcatalyst.exceptions import CatalystCacheError
from .. import _utils
from .._http_client import AuthorizedHttpClient
from .._constants import (
    RequestMethod,
    CredentialUser,
    Components
)
from ._segment import Segment


class CacheService(Component):
    def __init__(self, app) -> None:
        self._app = app
        self._requester = AuthorizedHttpClient(self._app)

    def get_component_name(self):
        return Components.CACHE

    def get_all_segment(self):
        resp = self._requester.request(
            method=RequestMethod.GET,
            path='/segment',
            user=CredentialUser.ADMIN
        )
        data: List = resp.response_json.get('data')
        segments: List[Segment] = []
        for segment in data:
            segments.append(Segment(self, segment))
        return segments

    def get_segment_details(self, seg_id: Union[str, int]):
        if not seg_id or not isinstance(seg_id, (int, str)):
            raise CatalystCacheError(
                'INVALID_SEGMENT_ID',
                'Segment Id must be a non empty string or number'
            )
        resp = self._requester.request(
            method=RequestMethod.GET,
            path=f'/segment/{seg_id}',
            user=CredentialUser.ADMIN
        )
        data = resp.response_json.get('data')
        return Segment(self, data)

    def segment(self, seg_id: Union[str, int] = None):
        if seg_id is None:
            return Segment(self, None)
        if not seg_id or not isinstance(seg_id, (int, str)):
            raise CatalystCacheError(
                'INVALID_SEGMENT_ID',
                'Segment Id must be a non empty string or number'
            )
        return Segment(self, {'id': seg_id})


def instance(app=None) -> CacheService:
    return _utils.get_ensured_app_service(app, Components.CACHE, CacheService)

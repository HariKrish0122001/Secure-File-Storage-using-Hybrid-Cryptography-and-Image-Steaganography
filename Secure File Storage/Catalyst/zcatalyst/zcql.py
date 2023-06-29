from typing import Dict, List, TypedDict
from zcatalyst.types import Component
from zcatalyst.exceptions import CatalystZCQLError
from . import _utils
from ._http_client import AuthorizedHttpClient
from ._constants import RequestMethod, CredentialUser, Components

ZcqlQueryOutput = TypedDict('ZcqlQueryOutput', {'table_name': Dict})


class ZcqlService(Component):
    def __init__(self, app) -> None:
        self._app = app
        self._requester = AuthorizedHttpClient(self._app)

    def get_component_name(self):
        return Components.ZCQL

    def execute_query(self, query: str) -> List[ZcqlQueryOutput]:
        if not query or not isinstance(query, str):
            raise CatalystZCQLError(
                'INVALID_QUERY',
                'Query must be a non empty string'
            )
        req_json = {
            'query': query
        }
        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/query',
            json=req_json,
            user=CredentialUser.USER
        )
        resp_json = resp.response_json
        return resp_json.get('data')


def instance(app=None) -> ZcqlService:
    return _utils.get_ensured_app_service(app, Components.ZCQL, ZcqlService)

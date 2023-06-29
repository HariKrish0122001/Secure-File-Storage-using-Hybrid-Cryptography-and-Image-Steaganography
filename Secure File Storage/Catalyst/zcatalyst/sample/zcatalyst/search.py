from typing import Dict, List, Any
from zcatalyst.types import Component, ICatalystSearchQuery
from . import _utils
from ._http_client import AuthorizedHttpClient
from ._constants import RequestMethod, CredentialUser, Components
from .exceptions import CatalystSearchError


class SearchService(Component):
    def __init__(self, app) -> None:
        self._app = app
        self._requester = AuthorizedHttpClient(self._app)

    def get_component_name(self):
        return Components.SEARCH

    def execute_search_query(
            self,
            query: ICatalystSearchQuery
    ) -> Dict[str, List[Dict[str, Any]]]:
        if not isinstance(query, dict) or not query:
            raise CatalystSearchError(
                'Invalid query object',
                'Query object must be a non empty dict'
            )
        for key in ['search', 'search_table_columns']:
            if not query.get(key):
                raise CatalystSearchError(
                    'Invalid query object',
                    f"Either the key '{key}' is missing or the value provided for the key is empty"
                )
        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/search',
            json=query,
            user=CredentialUser.USER
        )
        return resp.response_json.get('data')


def instance(app=None) -> SearchService:
    return _utils.get_ensured_app_service(app, Components.SEARCH, SearchService)

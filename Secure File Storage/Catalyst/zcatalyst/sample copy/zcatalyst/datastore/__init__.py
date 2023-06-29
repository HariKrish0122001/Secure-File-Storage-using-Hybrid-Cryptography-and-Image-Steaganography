from typing import Union, List
from zcatalyst.types import Component
from zcatalyst.exceptions import CatalystDatastoreError
from .. import _utils
from .._http_client import AuthorizedHttpClient
from ._table import Table
from .._constants import (
    RequestMethod,
    CredentialUser,
    Components
)


class DatastoreService(Component):
    def __init__(self, app) -> None:
        self._app = app
        self._requester = AuthorizedHttpClient(self._app)

    def get_component_name(self):
        return Components.DATA_STORE

    def get_all_tables(self):
        resp = self._requester.request(
            method=RequestMethod.GET,
            path='/table',
            user=CredentialUser.USER
        )
        data: List = resp.response_json.get('data')
        tables: List[Table] = []
        for table in data:
            tables.append(Table(self, table))
        return tables

    def get_table_details(self, table_id: Union[str, int]):
        if not table_id or not isinstance(table_id, (int, str)):
            raise CatalystDatastoreError(
                'INVALID_TABLE_ID',
                'Table Id must be a non empty string or number'
            )
        resp = self._requester.request(
            method=RequestMethod.GET,
            path=f'/table/{table_id}',
            user=CredentialUser.USER
        )
        data = resp.response_json.get('data')
        return Table(self, data)

    def table(self, table_id: Union[str, int]):
        if not table_id or not isinstance(table_id, (int, str)):
            raise CatalystDatastoreError(
                'INVALID_ARGUMENT',
                'Table Id/Table name must be a non empty string or number'
            )
        try:
            return Table(self, {'table_id': int(table_id)})
        except ValueError:
            return Table(self, {'table_name': str(table_id)})


def instance(app=None) -> DatastoreService:
    return _utils.get_ensured_app_service(app, Components.DATA_STORE, DatastoreService)

from typing import Any, Dict, List, TypedDict, Union
from zcatalyst.exceptions import CatalystDatastoreError
from zcatalyst.types import (
    ICatalystColumn,
    ICatalystRow,
    ICatalystRows,
    ParsableComponent
)
from .._constants import (
    RequestMethod,
    CredentialUser,
    Components
)

ICatalystRowInput = TypedDict('ICatalystRowInput', {'ROWID': str})


class Table(ParsableComponent):
    def __init__(self, datastore_instance, table_details: Dict):
        if not table_details or not isinstance(table_details, dict):
            raise CatalystDatastoreError(
                'INVALID_TABLE_DETAILS',
                'table_details must be a non empty dict'
            )
        self._requester = datastore_instance._requester
        self._identifier = table_details.get('table_id') or table_details.get('table_name')
        self._table_details = table_details

    def __repr__(self) -> str:
        return str(self._table_details)

    def get_component_name(self):
        return Components.DATA_STORE

    def get_all_columns(self) -> List[ICatalystColumn]:
        resp = self._requester.request(
            method=RequestMethod.GET,
            path=f'/table/{self._identifier}/column',
            user=CredentialUser.USER
        )
        resp_json = resp.response_json
        return resp_json.get('data')

    def get_column_details(self, col_id: Union[str, int]) -> ICatalystColumn:
        if not col_id or not isinstance(col_id, (int, str)):
            raise CatalystDatastoreError(
                'INVALID_COLUMN_ID',
                'Column Id must be a non empty string or number'
            )
        resp = self._requester.request(
            method=RequestMethod.GET,
            path=f'/table/{self._identifier}/column/{col_id}',
            user=CredentialUser.USER
        )
        resp_json = resp.response_json
        return resp_json.get('data')

    def insert_row(self, row: Dict[str, Any]) -> ICatalystRow:
        if not row or not isinstance(row, dict):
            raise CatalystDatastoreError(
                'INVALID_ROW_DATA',
                'Row data must be a non empty dict'
            )
        resp = self.insert_rows([row])
        return resp[0]

    def insert_rows(self, row_list: List[Dict]) -> List[ICatalystRow]:
        Table._validate_row_input(row_list)
        resp = self._requester.request(
            method=RequestMethod.POST,
            path=f'/table/{self._identifier}/row',
            json=row_list,
            user=CredentialUser.USER
        )
        resp_json = resp.response_json
        return resp_json.get('data')

    def get_paged_rows(
            self,
            next_token: str = None,
            max_rows: int = None
    ) -> ICatalystRows:
        req_params = {
            'next_token': next_token,
            'max_rows': max_rows
        }

        resp = self._requester.request(
            method=RequestMethod.GET,
            path=f'/table/{self._identifier}/row',
            params=req_params,
            user=CredentialUser.USER
        )

        resp_json = resp.response_json
        return resp_json

    def get_iterable_rows(self) -> List[ICatalystRow]:
        next_token: str = None
        while True:
            rows_output = self.get_paged_rows(next_token)
            for row in rows_output.get('data'):
                yield row
            next_token = rows_output.get('next_token')
            if next_token is None:
                break

    def get_row(self, row_id: Union[str, int]) -> ICatalystRow:
        if not row_id or not isinstance(row_id, (int, str)):
            raise CatalystDatastoreError(
                'INVALID_ROW_ID',
                'row id must be a non empty integer or string'
            )

        resp = self._requester.request(
            method=RequestMethod.GET,
            path=f'/table/{self._identifier}/row/{row_id}',
            user=CredentialUser.USER
        )

        resp_json = resp.response_json
        return resp_json.get('data')

    def delete_row(self, row_id: Union[str, int]) -> bool:
        if not row_id or not isinstance(row_id, (int, str)):
            raise CatalystDatastoreError(
                'INVALID_ROW_ID',
                'row id must be a non empty integer or string'
            )

        resp = self._requester.request(
            method=RequestMethod.DELETE,
            path=f'/table/{self._identifier}/row/{row_id}',
            user=CredentialUser.USER
        )

        resp_json = resp.response_json
        return bool(resp_json.get('data'))

    def delete_rows(self, ids: List[Union[str, int]]) -> bool:
        if not ids or not isinstance(ids, list):
            raise CatalystDatastoreError(
                'INVALID_ARGUMENT',
                'row ids cannot be empty and must be a instance of List[str|int]'
            )

        ids = list(map(str, ids))
        req_param = {
            'ids': ','.join(ids)
        }

        resp = self._requester.request(
            method=RequestMethod.DELETE,
            path=f'/table/{self._identifier}/row',
            params=req_param,
            user=CredentialUser.USER
        )
        resp_json = resp.response_json
        return bool(resp_json.get('data'))

    def update_row(self, row: ICatalystRowInput) -> ICatalystRow:
        if not row or not isinstance(row, dict):
            raise CatalystDatastoreError(
                'INVALID_ROW_DATA',
                'Row data must be a non empty dict'
            )
        resp = self.update_rows([row])
        return resp[0]

    def update_rows(self, row_list: List[ICatalystRowInput]) -> List[ICatalystRow]:
        Table._validate_row_input(row_list)
        resp = self._requester.request(
            method=RequestMethod.PATCH,
            path=f'/table/{self._identifier}/row',
            json=row_list,
            user=CredentialUser.USER
        )
        resp_json = resp.response_json
        return resp_json.get('data')

    @staticmethod
    def _validate_row_input(row_inputs: List[Dict]):
        if not row_inputs or not isinstance(row_inputs, list):
            raise CatalystDatastoreError(
                'INVALID_ARGUMENT',
                'Row inputs cannot be empty and must be a type of List[Dict]'
            )

    def to_dict(self):
        return self._table_details

    def to_string(self):
        return repr(self)

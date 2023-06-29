from typing import Dict, Union
from zcatalyst.types import Component
from zcatalyst.exceptions import CatalystCircuitError
from . import _utils
from ._http_client import AuthorizedHttpClient
from ._constants import RequestMethod, CredentialUser, Components


class CircuitService(Component):
    def __init__(self, app) -> None:
        self._app = app
        self._requester = AuthorizedHttpClient(self._app)

    def get_component_name(self):
        return Components.CIRCUIT

    def execute(
            self,
            circuit_id: Union[int, str],
            name: str,
            inputs: Dict[str, str] = None
    ):
        self._is_non_empty_string_or_num(circuit_id, 'circuit_id')
        self._is_non_empty_string(name, 'circuit_name')
        req_json = {
            'name': name,
            'input': inputs or {}
        }
        resp = self._requester.request(
            method=RequestMethod.POST,
            path=f'/circuit/{circuit_id}/execute',
            json=req_json,
            user=CredentialUser.ADMIN
        )
        return resp.response_json.get('data')

    def status(
            self,
            circuit_id: Union[int, str],
            exec_id: Union[int, str]
    ):
        self._is_non_empty_string_or_num(circuit_id, 'circuit_id')
        self._is_non_empty_string_or_num(exec_id, 'execution_id')
        resp = self._requester.request(
            method=RequestMethod.GET,
            path=f'/circuit/{circuit_id}/execution/{exec_id}',
            user=CredentialUser.ADMIN
        )
        return resp.response_json.get('data')

    def abort(
            self,
            circuit_id: Union[int, str],
            exec_id: Union[int, str]
    ):
        self._is_non_empty_string_or_num(circuit_id, 'circuit_id')
        self._is_non_empty_string_or_num(exec_id, 'execution_id')
        resp = self._requester.request(
            method=RequestMethod.DELETE,
            path=f'/circuit/{circuit_id}/execution/{exec_id}',
            user=CredentialUser.ADMIN
        )
        return resp.response_json.get('data')

    @staticmethod
    def _is_non_empty_string_or_num(var, attr_name):
        if not var or not isinstance(var, (int, str)):
            raise CatalystCircuitError(
                'Invalid-Argument',
                f'{attr_name} must be a non empty string or number'
            )

    @staticmethod
    def _is_non_empty_string(var, attr_name):
        if not var or not isinstance(var, str):
            raise CatalystCircuitError(
                'Invalid-Argument',
                f'{attr_name} must be a non empty string'
            )


def instance(app=None) -> CircuitService:
    return _utils.get_ensured_app_service(app, Components.CIRCUIT, CircuitService)

from typing import Dict, Union
from zcatalyst.types import Component
from zcatalyst.exceptions import CatalystFunctionError
from . import _utils
from ._http_client import AuthorizedHttpClient
from ._constants import RequestMethod, CredentialUser, Components


class FunctionService(Component):
    def __init__(self, app) -> None:
        self._app = app
        self._requester = AuthorizedHttpClient(self._app)

    def get_component_name(self):
        return Components.FUNCTION

    def execute(self, func_id: Union[str, int], args: Dict = None):
        if not func_id or not isinstance(func_id, (int, str)):
            raise CatalystFunctionError(
                'INVALID_FUNCTION_ID',
                'Function Id must be a non empty string or number'
            )
        if args and not isinstance(args, dict):
            raise CatalystFunctionError(
                'INVALID_ARGUMENTS',
                'Function Args must be a instance of dict'
            )
        resp = self._requester.request(
            method=RequestMethod.POST,
            path=f'/function/{func_id}/execute',
            json=args,
            user=CredentialUser.USER
        )
        resp_json = resp.response_json
        return str(resp_json.get('data')) or str(resp_json.get('output'))


def instance(app=None) -> FunctionService:
    return _utils.get_ensured_app_service(app, Components.FUNCTION, FunctionService)

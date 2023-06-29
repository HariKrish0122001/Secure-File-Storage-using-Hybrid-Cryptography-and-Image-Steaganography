from typing import Union, List
from zcatalyst.types import Component
from zcatalyst.exceptions import CatalystCronError
from .. import _utils
from .._http_client import AuthorizedHttpClient
from .._constants import (
    RequestMethod,
    CredentialUser,
    Components
)
from ._helper import (
    ICatalystCronReq,
    ICatalystCronRes,
    ICatalystCronUpdateReq
)


class CronService(Component):
    def __init__(self, app) -> None:
        self._app = app
        self._requester = AuthorizedHttpClient(self._app)

    def get_component_name(self):
        return Components.CRON

    def get_all_cron(self) -> List[ICatalystCronRes]:
        resp = self._requester.request(
            method=RequestMethod.GET,
            path='/cron',
            user=CredentialUser.ADMIN
        )
        resp_json = resp.response_json
        return resp_json.get('data')

    def get_cron_details(self, cron_id: Union[int, str]) -> ICatalystCronRes:
        if not cron_id or not isinstance(cron_id, (int, str)):
            raise CatalystCronError(
                'INVALID_CRON_ID',
                'cron id must be non empty string or number'
            )
        resp = self._requester.request(
            method=RequestMethod.GET,
            path=f'/cron/{cron_id}',
            user=CredentialUser.ADMIN
        )
        resp_json = resp.response_json
        return resp_json.get('data')

    def create_cron(self, cron_details: ICatalystCronReq) -> ICatalystCronRes:
        self._validate_cron(cron_details)
        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/cron',
            json=cron_details,
            user=CredentialUser.ADMIN
        )
        resp_json = resp.response_json
        return resp_json.get('data')

    def update_cron(self, cron_details: ICatalystCronUpdateReq) -> ICatalystCronRes:
        self._validate_cron(cron_details, {'id'})
        cron_id = cron_details.get('id')
        resp = self._requester.request(
            method=RequestMethod.PUT,
            path=f'/cron/{cron_id}',
            json=cron_details,
            user=CredentialUser.ADMIN
        )
        resp_json = resp.response_json
        return resp_json.get('data')

    def delete_cron(self, cron_id: Union[int, str]) -> bool:
        if not cron_id or not isinstance(cron_id, (int, str)):
            raise CatalystCronError(
                'INVALID_CRON_ID',
                'cron id must be non empty string or number'
            )
        resp = self._requester.request(
            method=RequestMethod.DELETE,
            path=f'/cron/{cron_id}',
            user=CredentialUser.ADMIN
        )
        resp_json = resp.response_json
        return bool(resp_json.get('data'))

    @staticmethod
    def _validate_cron(cron_details, mandatories=None):
        if not cron_details or not isinstance(cron_details, dict):
            raise CatalystCronError(
                'INVALID_CRON_DETAILS',
                'cron details must be passed as a non empty dict'
            )
        if mandatories:
            for mand in mandatories:
                if mand not in cron_details:
                    raise CatalystCronError(
                        'INVALID_CRON_DETAILS',
                        f'cron details must contain the mandatory keys {str(mandatories)}'
                    )


def instance(app=None) -> CronService:
    return _utils.get_ensured_app_service(app, Components.CRON, CronService)

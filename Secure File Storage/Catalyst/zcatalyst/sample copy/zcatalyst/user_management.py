from typing import List, Union
from zcatalyst.types import (
    Component,
    ICatalystSignupConfig,
    ICatalystUserDetails,
    ICatalystUser
)
from zcatalyst.exceptions import CatalystUserManagementError
from . import _utils
from ._http_client import AuthorizedHttpClient
from ._constants import RequestMethod, CredentialUser, Components


class ICatalystNewUser(ICatalystSignupConfig):
    user_details: ICatalystUser


class UserService(Component):
    def __init__(self, app) -> None:
        self._app = app
        self._requester = AuthorizedHttpClient(self._app)

    def get_component_name(self):
        return Components.USER_MANAGEMENT

    def get_current_user(self) -> ICatalystUser:
        resp = self._requester.request(
            method=RequestMethod.GET,
            path='/project-user/current',
            user=CredentialUser.USER
        )
        resp_json = resp.response_json
        return resp_json.get('data')

    def get_all_users(self) -> List[ICatalystUser]:
        resp = self._requester.request(
            method=RequestMethod.GET,
            path='/project-user',
            user=CredentialUser.ADMIN
        )
        resp_json = resp.response_json
        return resp_json.get('data')

    def get_user_details(self, user_id: Union[int, str]) -> ICatalystUser:
        if not user_id or not isinstance(user_id, (int, str)):
            raise CatalystUserManagementError(
                'INVALID_USER_ID',
                'User Id must be a non empty string or number'
            )
        resp = self._requester.request(
            method=RequestMethod.GET,
            path=f'/project-user/{user_id}',
            user=CredentialUser.ADMIN
        )
        resp_json = resp.response_json
        return resp_json.get('data')

    def delete_user(self, user_id: Union[int, str]) -> bool:
        if not user_id or not isinstance(user_id, (int, str)):
            raise CatalystUserManagementError(
                'INVALID_USER_ID',
                'User Id must be a non empty string or number'
            )
        resp = self._requester.request(
            method=RequestMethod.DELETE,
            path=f'/project-user/{user_id}',
            user=CredentialUser.ADMIN
        )
        resp_json = resp.response_json
        return bool(resp_json.get('data'))

    def register_user(
            self,
            signup_config: ICatalystSignupConfig,
            user_details: ICatalystUserDetails
    ) -> ICatalystNewUser:
        self._validate_signup_config(signup_config, {'platform_type', 'zaid'})
        self._validate_user_details(user_details, {'last_name', 'email_id'})
        signup_config['user_details'] = user_details
        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/project-user/signup',
            json=signup_config,
            user=CredentialUser.USER
        )
        resp_json = resp.response_json
        return resp_json.get('data')

    def add_user_to_org(
            self,
            signup_config: ICatalystSignupConfig,
            user_details: ICatalystUserDetails
    ) -> ICatalystNewUser:
        self._validate_signup_config(signup_config, {'platform_type'})
        #self._validate_user_details(user_details, {'last_name', 'email_id'})
        signup_config['user_details'] = user_details
        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/project-user',
            json=signup_config,
            user=CredentialUser.ADMIN
        )
        resp_json = resp.response_json
        return resp_json.get('data')

    def reset_password(
            self,
            signup_config: ICatalystSignupConfig,
            user_details: ICatalystUserDetails
    ) -> str:
        self._validate_signup_config(signup_config, {'platform_type', 'zaid'})
        self._validate_user_details(user_details, {'email_id'})
        signup_config['user_details'] = user_details
        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/project-user/forgotpassword',
            json=signup_config,
            user=CredentialUser.USER
        )
        resp_json = resp.response_json
        return resp_json.get('data')

    @staticmethod
    def _validate_signup_config(signup_config, mandatories):
        if not signup_config or not isinstance(signup_config, dict):
            raise CatalystUserManagementError(
                'INVALID_SIGNUP_CONFIG',
                'signup config must be a non empty dict'
            )
        if not mandatories <= signup_config.keys():
            raise CatalystUserManagementError(
                'INVALID_SIGNUP_CONFIG',
                f'signup config must contain the mandatory keys {str(mandatories)}'
            )

    @staticmethod
    def _validate_user_details(user_details, mandatories):
        if not user_details or not isinstance(user_details, dict):
            raise CatalystUserManagementError(
                'INVALID_USER_DETAILS',
                'User details must be a non empty dict'
            )
        if not mandatories <= user_details.keys():
            raise CatalystUserManagementError(
                'INVALID_SIGNUP_CONFIG',
                f'signup config must contain the mandatory keys {str(mandatories)}'
            )


def instance(app=None) -> UserService:
    return _utils.get_ensured_app_service(app, Components.USER_MANAGEMENT, UserService)

from typing import Union, List
from zcatalyst.types import Component
from zcatalyst.exceptions import CatalystFilestoreError
from .. import _utils
from .._http_client import AuthorizedHttpClient
from .._constants import RequestMethod, CredentialUser, Components
from ._folder import Folder


class FilestoreService(Component):
    def __init__(self, app) -> None:
        self._app = app
        self._requester = AuthorizedHttpClient(self._app)

    def get_component_name(self):
        return Components.FILE_STORE

    def create_folder(self, name: str):
        if not name or not isinstance(name, str):
            raise CatalystFilestoreError(
                'INVALID_FOLDER_NAME',
                'Folder name must be a non empty string'
            )
        req_json = {
            'folder_name': name
        }

        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/folder',
            json=req_json,
            user=CredentialUser.ADMIN
        )
        resp_json = resp.response_json
        data = resp_json.get('data')
        return Folder(self, data)

    def get_all_folders(self):
        resp = self._requester.request(
            method=RequestMethod.GET,
            path='/folder',
            user=CredentialUser.USER
        )
        data: List = resp.response_json.get('data')
        folders: List[Folder] = []
        for folder in data:
            folders.append(Folder(self, folder))
        return folders

    def get_folder_details(self, folder_id: Union[int, str]):
        if not folder_id or not isinstance(folder_id, (str, int)):
            raise CatalystFilestoreError(
                'INVALID_FOLDER_ID',
                'Folder id must be a non empty string or number'
            )
        resp = self._requester.request(
            method=RequestMethod.GET,
            path=f'/folder/{folder_id}',
            user=CredentialUser.USER
        )
        resp_json = resp.response_json
        data = resp_json.get('data')
        return Folder(self, data)

    def folder(self, folder_id: Union[int, str]):
        if not id or not isinstance(folder_id, (str, int)):
            raise CatalystFilestoreError(
                'INVALID_FOLDER_ID',
                'Folder id must be a non empty string or number'
            )
        return Folder(self, {'id': folder_id})


def instance(app=None) -> FilestoreService:
    return _utils.get_ensured_app_service(app, Components.FILE_STORE, FilestoreService)

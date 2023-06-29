from io import BufferedReader
from typing import Dict, TypedDict, Union
from urllib3.response import HTTPResponse
from zcatalyst.types import ParsableComponent
from ..exceptions import CatalystFilestoreError
from .._constants import (
    RequestMethod,
    CredentialUser,
    Components
)
from ._helper import (
    ICatalystFileDetails,
    ICatalystFolderDetails,
    ICatalystFileInput
)

ICatalystFolderUpdateDetails = TypedDict('ICatalystUpdateReq', {'folder_name': str})


class Folder(ParsableComponent):
    def __init__(self, filestore_instance, folder_details: Dict):
        if not folder_details or not isinstance(folder_details, dict):
            raise CatalystFilestoreError(
                'INVALID_FOLDER_DETAILS',
                'folder details must be a non empty dict'
            )
        self._requester = filestore_instance._requester
        self._folder_details = folder_details
        self._id = folder_details.get('id')

    def __repr__(self) -> str:
        return str(self._folder_details)

    def get_component_name(self):
        return Components.FILE_STORE

    def update(self, folder_details: ICatalystFolderUpdateDetails) -> ICatalystFolderDetails:
        folder_name = folder_details['folder_name']
        if not folder_name or not isinstance(folder_name, str):
            raise CatalystFilestoreError(
                'INVALID_FOLDER_NAME',
                'Folder name must be a non empty string'
            )
        resp = self._requester.request(
            method=RequestMethod.PUT,
            path=f'/folder/{self._id}',
            json=folder_details,
            user=CredentialUser.ADMIN
        )
        resp_json = resp.response_json
        return resp_json.get('data')

    def delete(self):
        resp = self._requester.request(
            method=RequestMethod.DELETE,
            path=f'/folder/{self._id}',
            user=CredentialUser.ADMIN
        )
        resp_json = resp.response_json
        return bool(resp_json.get('data'))

    def get_file_details(self, file_id: Union[int, str]) -> ICatalystFileDetails:
        if not file_id or not isinstance(file_id, (str, int)):
            raise CatalystFilestoreError(
                'INVALID_FILE_ID',
                'File id must be a non empty string or number'
            )
        resp = self._requester.request(
            method=RequestMethod.GET,
            path=f'/folder/{self._id}/file/{file_id}',
            user=CredentialUser.USER
        )
        resp_json = resp.response_json
        return resp_json.get('data')

    def delete_file(self, file_id: Union[int, str]) -> bool:
        if not file_id or not isinstance(file_id, (str, int)):
            raise CatalystFilestoreError(
                'INVALID_FILE_ID',
                'File id must be a non empty string or number'
            )
        resp = self._requester.request(
            method=RequestMethod.DELETE,
            path=f'/folder/{self._id}/file/{file_id}',
            user=CredentialUser.USER
        )
        resp_json = resp.response_json
        return bool(resp_json.get('data'))

    def upload_file(
            self,
            file_details: ICatalystFileInput
    ) -> ICatalystFileDetails:
        Folder._validate_file_details(file_details)
        # data = [
        #     ('code',('',file_details['code'],'application/octet-stream')),
        #     ('file_name',(None,file_details['name']))
        # ]
        resp = self._requester.request(
            method=RequestMethod.POST,
            path=f'/folder/{self._id}/file',
            files={
                'code': ('', file_details['code'], 'application/octet-stream')
            },
            data={
                'file_name': file_details['name']
            },
            user=CredentialUser.USER
        )
        resp_json = resp.response_json
        return resp_json.get('data')

    def download_file(self, file_id: Union[int, str]):
        if not file_id or not isinstance(file_id, (str, int)):
            raise CatalystFilestoreError(
                'INVALID_FILE_ID',
                'File id must be a non empty string or number'
            )
        resp = self._requester.request(
            method=RequestMethod.GET,
            path=f'/folder/{self._id}/file/{file_id}/download',
            user=CredentialUser.USER,
            stream=True
        )
        return resp._response.content  # pylint: disable=protected-access

    def get_file_stream(self, file_id: Union[int, str]) -> HTTPResponse:
        if not file_id or not isinstance(file_id, (str, int)):
            raise CatalystFilestoreError(
                'INVALID_FILE_ID',
                'File id must be a non empty string or number'
            )
        resp = self._requester.request(
            method=RequestMethod.GET,
            path=f'/folder/{self._id}/file/{file_id}/download',
            user=CredentialUser.USER,
            stream=True
        )
        return resp._response.raw  # pylint: disable=protected-access

    @staticmethod
    def _validate_file_details(file_details):
        if not file_details or not isinstance(file_details, dict):
            raise CatalystFilestoreError(
                'INVALID_FILE_DETAILS',
                'File details must be a non empty dict'
            )
        if not isinstance(file_details.get('code'), BufferedReader):
            raise CatalystFilestoreError(
                'INVALID_FILE_DETAILS',
                'Code cannot be empty and must be a instance of BufferReader'
            )
        name = file_details.get('name')
        if not name or not isinstance(name, str):
            raise CatalystFilestoreError(
                'INVALID_FILE_DETAILS',
                'name in file details must be a non empty string'
            )

    def to_string(self):
        return repr(self)

    def to_dict(self) -> ICatalystFolderDetails:
        return self._folder_details

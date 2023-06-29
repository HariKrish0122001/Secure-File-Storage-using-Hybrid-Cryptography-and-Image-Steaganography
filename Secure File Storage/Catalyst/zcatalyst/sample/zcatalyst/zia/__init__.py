from io import BufferedReader
from typing import Any, Dict, List, Optional, Union
from .. import _utils
from ..types import Component
from .._http_client import AuthorizedHttpClient
from ..exceptions import CatalystZiaError
from .._constants import Components, RequestMethod, CredentialUser
from ..types.zia import (
    ICatalystZiaKeywordExtraction,
    ICatalystZiaBarcode,
    ICatalystZiaFace,
    ICatalystZiaFaceComparison,
    ICatalystZiaModeration,
    ICatalystZiaOCR,
    ICatalystZiaObject,
    ICatalystZiaSentimentAnalysis
)
from ._helper import (
    ICatalystOCROptions,
    ICatalystImageModerationOpts,
    ICatalystBarCodeOptions,
    ICatalystFaceAnalysisOptions
)


class ZiaService(Component):
    def __init__(self, app):
        self._app = app
        self._requester = AuthorizedHttpClient(app)

    def get_component_name(self):
        return Components.ZIA

    def detect_object(
            self,
            file: BufferedReader
    ) -> ICatalystZiaObject:
        self._is_valid_file_type(file)
        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/ml/detect-object',
            files={
                'image': file
            },
            user=CredentialUser.ADMIN
        )
        return resp.response_json.get('data')

    def extract_optical_characters(
            self,
            file: BufferedReader,
            options: ICatalystOCROptions = None
    ) -> ICatalystZiaOCR:
        self._is_valid_file_type(file)
        resp = self._requester.request(
            method=RequestMethod.POST,
            path='ml/ocr',
            files={
                'image': file
            },
            data=options,
            user=CredentialUser.ADMIN
        )
        return resp.response_json.get('data')

    def extract_aadhaar_characters(
            self,
            front_img: BufferedReader,
            back_img: BufferedReader,
            language: str
    ) -> ICatalystZiaOCR:
        self._is_valid_file_type(front_img, back_img)
        if not isinstance(language, str) or not language:
            raise CatalystZiaError(
                'Invalid-Argument',
                'Value provided for language is expected to be a non empty string'
            )
        resp = self._requester.request(
            method=RequestMethod.POST,
            path='ml/ocr',
            files={
                'aadhaar_front': front_img,
                'aadhaar_back': back_img
            },
            data={
                'language': language,
                'model_type': 'AADHAAR'
            },
            user=CredentialUser.ADMIN
        )
        return resp.response_json.get('data')

    def scan_barcode(
            self,
            image: BufferedReader,
            options: ICatalystBarCodeOptions = None
    ) -> ICatalystZiaBarcode:
        self._is_valid_file_type(image)
        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/ml/barcode',
            files={
                'image': image
            },
            data=options,
            user=CredentialUser.ADMIN
        )
        return resp.response_json.get('data')

    def moderate_image(
            self,
            image: BufferedReader,
            options: ICatalystImageModerationOpts = None
    ) -> ICatalystZiaModeration:
        self._is_valid_file_type(image)
        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/ml/imagemoderation',
            files={
                'image': image
            },
            data=options,
            user=CredentialUser.ADMIN
        )
        return resp.response_json.get('data')

    def analyse_face(
            self,
            image: BufferedReader,
            options: ICatalystFaceAnalysisOptions = None
    ) -> ICatalystZiaFace:
        self._is_valid_file_type(image)
        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/ml/faceanalytics',
            files={
                'image': image
            },
            data=options,
            user=CredentialUser.ADMIN
        )
        return resp.response_json.get('data')

    def compare_face(
            self,
            source_img: BufferedReader,
            query_img: BufferedReader
    ) -> ICatalystZiaFaceComparison:
        self._is_valid_file_type(source_img, query_img)
        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/ml/facecomparison',
            files={
                'source_image': source_img,
                'query_image': query_img
            },
            user=CredentialUser.ADMIN
        )
        return resp.response_json.get('data')

    def auto_ml(
            self,
            model_id: Union[int, str],
            data: Dict[str, Any] = None
    ):
        if not model_id or not isinstance(model_id, (int, str)):
            raise CatalystZiaError(
                'Invalid-Argument',
                'Model id should be a non empty string or number'
            )
        resp = self._requester.request(
            method=RequestMethod.POST,
            path=f'/ml/automl/model/{model_id}',
            json=data,
            user=CredentialUser.ADMIN
        )
        return resp.response_json.get('data')

    def get_sentiment_analysis(
            self,
            list_of_docs: List[str],
            keywords: Optional[List[str]] = None
    ) -> ICatalystZiaSentimentAnalysis:
        self._is_non_empty_list(list_of_docs, 'documents list')
        if keywords:
            self._is_non_empty_list(keywords, 'keywords')
        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/ml/text-analytics/sentiment-analysis',
            json={
                'document': list_of_docs,
                'keywords': keywords
            },
            user=CredentialUser.ADMIN,
        )
        return resp.response_json.get('data')

    def get_keyword_extraction(
            self,
            list_of_docs: List[str]
    ) -> ICatalystZiaKeywordExtraction:
        self._is_non_empty_list(list_of_docs, 'documents list')
        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/ml/text-analytics/keyword-extraction',
            json={
                'document': list_of_docs
            },
            user=CredentialUser.ADMIN,
        )
        return resp.response_json.get('data')

    def get_NER_prediction(  # pylint: disable=invalid-name
            self,
            list_of_docs: List[str]
    ) -> ICatalystZiaKeywordExtraction:
        self._is_non_empty_list(list_of_docs, 'documents list')
        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/ml/text-analytics/ner',
            json={
                'document': list_of_docs
            },
            user=CredentialUser.ADMIN,
        )
        return resp.response_json.get('data')

    def get_text_analytics(
            self,
            list_of_docs: List[str],
            keywords: Optional[List[str]] = None
    ) -> ICatalystZiaSentimentAnalysis:
        self._is_non_empty_list(list_of_docs, 'documents list')
        if keywords:
            self._is_non_empty_list(keywords, 'keywords')
        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/ml/text-analytics',
            json={
                'document': list_of_docs,
                'keywords': keywords
            },
            user=CredentialUser.ADMIN,
        )
        return resp.response_json.get('data')

    @staticmethod
    def _is_non_empty_list(arr, attr_name: str):
        if not isinstance(arr, list) or not arr:
            raise CatalystZiaError(
                'Invalid-Argument',
                f'The value for {attr_name} is expected to be a non empty list'
            )

    @staticmethod
    def _is_valid_file_type(*files):
        for file in files:
            if not isinstance(file, BufferedReader):
                raise CatalystZiaError(
                    'Invalid-Argument',
                    'File must be a instance of BufferReader'
                )


def instance(app=None) -> ZiaService:
    return _utils.get_ensured_app_service(app, Components.ZIA, ZiaService)

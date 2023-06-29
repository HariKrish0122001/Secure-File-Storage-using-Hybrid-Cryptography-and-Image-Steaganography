from typing import Union
from zcatalyst.types import Component
from zcatalyst.exceptions import CatalystPushNotificationError
from .. import _utils
from .._http_client import AuthorizedHttpClient
from .._constants import Components
from ._web_notificaton import WebNotification
from ._mobile_notification import MobileNotification


class PushNotificationService(Component):
    def __init__(self, app):
        self._app = app
        self._requester = AuthorizedHttpClient(app)

    def get_component_name(self):
        return Components.PUSH_NOTIFICATION

    def mobile(self, app_id: Union[int, str]):
        if not id or not isinstance(id, (int, str)):
            raise CatalystPushNotificationError(
                'Invalid Argument',
                'Value provided for app_id must be a non empty string or number'
            )
        return MobileNotification(self, str(app_id))

    def web(self):
        return WebNotification(self)


def instance(app=None) -> PushNotificationService:
    return _utils.get_ensured_app_service(
        app, Components.PUSH_NOTIFICATION, PushNotificationService
    )

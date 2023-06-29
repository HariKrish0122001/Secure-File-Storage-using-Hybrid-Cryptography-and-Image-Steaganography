from typing import List
from zcatalyst.exceptions import CatalystPushNotificationError
from .._constants import (
    RequestMethod,
    CredentialUser
)


class WebNotification:
    def __init__(self, notification_instance):
        self._app = notification_instance._app
        self._requester = notification_instance._requester

    def send_notification(
            self,
            message: str,
            recipients: List[str]
    ) -> bool:
        if not message or not isinstance(message, str):
            raise CatalystPushNotificationError(
                'Invalid Argument',
                'Value provided for message is expected to be a not empty string',
                message
            )
        if not recipients or not isinstance(recipients, list):
            raise CatalystPushNotificationError(
                'Invalid Argument',
                'Value provided for recipients is expected to be a not empty list',
                recipients
            )
        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/project-user/notify',
            json={
                'message': message,
                'recipients': recipients
            },
            user=CredentialUser.ADMIN
        )
        return resp.response_json.get('data')

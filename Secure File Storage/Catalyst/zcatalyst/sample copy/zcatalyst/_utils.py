from zcatalyst import get_app, CatalystApp
from zcatalyst.exceptions import CatalystAppError


def get_ensured_app_service(app, service_name, initializer, **kwargs):
    if app is None:
        app = get_app()
    else:
        # if app provided by user, check whether it is valid zcatalyst app
        if not isinstance(app, CatalystApp):
            raise CatalystAppError(
                'INVALID_APP',
                'App must be a type of CatalystApp'
            )
    return app._ensure_service(service_name, initializer, **kwargs)  # pylint: disable=protected-access

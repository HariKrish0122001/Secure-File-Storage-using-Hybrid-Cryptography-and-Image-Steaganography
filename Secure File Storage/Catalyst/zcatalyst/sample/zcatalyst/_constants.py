import os


def env_override(env_name: str, default_value: str):
    env_value = os.getenv(env_name)
    if not env_value:
        return default_value
    return env_value


# SDK version
SDK_VERSION = "0.1.0"

# Json variables
JSON_RESPONSE_KEY = "data"
JSON_RESPONSE_STATUS = "status"
JSON_RESPONSE_MESSAGE = "message"
JSON_RESPONSE_CODE = "error_code"
SUCCESS_STATUS = "success"
FAILURE_STATUS = "failure"

# Environment Variable
PROJECT_KEY = "project_key"
PROJECT_ID = "project_id"
PROJECT_DOMAIN = "project_domain"
ENVIRONMENT = "environment"
PROJECT_SECRET_KEY = "project_secret_key"
ADMIN_CRED = "admin_cred"
CLIENT_CRED = "client_cred"
COOKIE_CRED = "cookien_cred"
ACCESS_TOKEN = "access_token"
CLIENT_ACCESS_TOKEN = "client_token"
CLIENT_COOKIE = "client_cookie"
CLIENT_ID = "client_id"
EXPIRES_IN = "expires_in"
CLIENT_SECRET = "client_secret"
AUTH_URL = "auth_url"
REFRESH_URL = "refresh_url"
REDIRECT_URL = "redirect_url"
GRANT_TYPE = "grant_type"
CODE = "code"
TICKET = "ticket"
ADMIN_CRED_TYPE = "admin_cred_type"
CLIENT_CRED_TYPE = "client_cred_type"
REFRESH_TOKEN = "refresh_token"
USER_TYPE = "user_type"
CONNECTOR_NAME = "connector_name"

# URL constants
PROJECT_URL = "project"
PROJECT_KEY_NAME = "PROJECT_ID"
FILE_SEPERATOR = "/"
IS_LOCAL = env_override("X_ZOHO_CATALYST_IS_LOCAL", "False")
CSRF_TOKEN_COOKIE = "ZD_CSRF_TOKEN"
APP_DOMAIN =  "https://consoleinteg.catalyst.localzoho.com"
APP_BAAS = "/baas"
APP_VERSION_V1 = "/v1"
APP_BASE_URL = APP_DOMAIN + APP_BAAS + APP_VERSION_V1
ACCOUNTS_URL = env_override("X_ZOHO_CATALYST_ACCOUNTS_URL", "https://accounts.localzoho.com")

# Header Constants
CONTENT_TYPE = "Content-Type"
CLIENT_HEADER = "PROJECT_ID"
COOKIE_HEADER = "Cookie"
CSRF_HEADER = "X-ZCSRF-TOKEN"
USER_AGENT = "USER-AGENT"

# Auth Constants
AUTHORIZATION = "Authorization"
COOKIE = "cookie"
USER_SCOPE_HEADER = "X-CATALYST-USER"
ADMIN_SCOPE = "admin"
USER_SCOPE = "user"
OAUTH_PREFIX = "Zoho-oauthtoken "
TICKET_PREFIX = "Zoho-ticket "
CSRF_PARAM_PREFIX = "zd_csrparam="


class AcceptHeader:
    KEY = 'Accept'
    VALUE = 'application/vnd.catalyst.v2+json'


class InitType:
    ADVANCED_IO = 'advancedio'
    BASIC_IO = 'basicio'


ENVIRONMENT_KEY_NAME = "X-Catalyst-Environment"
USER_KEY_NAME = "X-CATALYST-USER"


class CredentialUser:
    ADMIN = 'admin'
    USER = 'user'


class RequestMethod:
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class Components:
    CACHE = "Cache"
    FILE_STORE = "FileStore"
    MAIL = "Mail"
    SEARCH = "Search"
    ZCQL = "ZCQL"
    ZIA = "Zia"
    CRON = "Cron"
    DATA_STORE = "DataStore"
    FUNCTION = "Function"
    USER_MANAGEMENT = "UserManagement"
    CIRCUIT = "Circuit"
    PUSH_NOTIFICATION = "PushNotification"


class CredentialType:
    token = 'token'
    ticket = 'ticket'


class ProjectHeader:
    project_id = 'x-zc-projectid'
    domain = 'x-zc-project-domain'
    key = 'x-zc-project-key'
    environment = 'x-zc-environment'
    project_secret_key = 'x-zc-project-secret-key'


class CredentialHeader:
    admin_cred_type = 'x-zc-admin-cred-type'
    user_cred_type = 'x-zc-user-cred-type'
    admin_token = 'x-zc-admin-cred-token'
    user_token = 'x-zc-user-cred-token'
    cookie = 'x-zc-cookie'
    zcsrf = 'X-ZCSRF-TOKEN'
    user = 'x-zc-user-type'

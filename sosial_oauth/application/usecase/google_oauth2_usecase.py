from account.adapter.input.web.request.create_account_request import CreateAccountRequest
from account.application.usecase.account_usecase import AccountUseCase
from sosial_oauth.adapter.input.web.request.get_access_token_request import GetAccessTokenRequest
from sosial_oauth.adapter.input.web.response.access_token import AccessToken
from sosial_oauth.infrastructure.service.google_oauth2_service import GoogleOAuth2Service

account_usecase = AccountUseCase().get_instance()

class GoogleOAuth2UseCase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    @staticmethod
    def get_authorization_url() -> str:
        return GoogleOAuth2Service.get_authorization_url()

    async def login_and_fetch_user(self, state: str, code: str) -> AccessToken:
        try:
            # 1. Access token 획득
            access_token = self._fetch_access_token(state, code)

            return access_token
        except Exception as e:
            raise Exception(f"Failed to login and fetch user: {str(e)}") from e



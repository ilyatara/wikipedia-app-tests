import os
from typing import Literal

from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional
from dotenv import find_dotenv
from appium.options.android import UiAutomator2Options

import utils


class Config(BaseSettings):

    context: Literal['bstack', 'local_real', 'local_emulator']

    remote_url: str

    device_name: str
    platform_version: str

    app: str
    app_wait_activity: str

    language: Optional[str] = None
    locale: Optional[str] = None

    bstack_username: Optional[str] = None
    bstack_access_key: Optional[str] = None
    bstack_project_name: Optional[str] = None
    bstack_build_name: Optional[str] = None
    bstack_session_name: Optional[str] = None

    timeout: float = Field(alias='selene_timeout', default=10.0)

    @staticmethod
    def get_context():
        return os.getenv('context')

    def to_driver_options(self):
        options = UiAutomator2Options()

        options.set_capability('deviceName', self.device_name)
        options.set_capability('platformVersion', self.platform_version)
        options.set_capability('appWaitActivity', self.app_wait_activity)

        options.set_capability('language', self.language)
        options.set_capability('locale', self.locale)

        if self.context == 'bstack':
            options.set_capability('app', self.app)
            options.set_capability(
                'bstack:options', {
                    'projectName': self.bstack_project_name,
                    'buildName': self.bstack_build_name,
                    'sessionName': self.bstack_session_name,
                    'userName': self.bstack_username,
                    'accessKey': self.bstack_access_key
                },
            )
        else:
            options.set_capability('app', utils.path.get_path(self.app))

        return options


config = Config(_env_file=find_dotenv(f'.env.{Config.get_context()}'))

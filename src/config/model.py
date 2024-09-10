"""
This module sets up the model configuration.

It utilizes Pydantic's BaseSettings for configuration management,
allowing settings to be read from environment variables and a .env file.
"""

from loguru import logger
from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModelSettings(BaseSettings):
    """
    ML model configuration settings for the application.

    Attributes:
        model_config (SettingsConfigDict): Model config, loaded from .env file.
        model_path (DirectoryPath): Filesystem path to the model.
        model_name (str): Name of the ML model.
    """

    model_config = SettingsConfigDict(
        env_file='config/.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )
    model_config['protected_namespaces'] = ('settings_',)

    model_path: DirectoryPath
    model_name: str


# Initializing model settings
model_settings = ModelSettings()
# Logging model settings
logger.info(f'Model settings: {model_settings}')

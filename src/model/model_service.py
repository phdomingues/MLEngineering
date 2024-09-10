"""
This module provides functionality for managing a ML model.

It contains the ModelService class, which handles loading and using
a pre-trained ML model. The class offers methods to load a model
from a file, building it if it doesn't exist, and to make predictions
using the loaded model.
"""

import pickle as pk
from pathlib import Path

from loguru import logger

from config import model_settings
from model.pipeline.model import build_model


class ModelService:
    """
    A service class for managing the ML model.

    This class provides functionalities to load a ML model from
    a specified path, build it if it doesn't exist, and make
    predictions using the loaded model.

    Attributes:
        model: ML model managed by this service. Initially set to None.

    Methods:
        __init__: Constructor to initialize the ModelService.
        load_model: Load from file or builds it if it doesn't exist.
        predict: Makes a prediction using the loaded model.
    """

    def __init__(self) -> None:
        """Initializes the ModelService with no models loaded."""
        self.model = None

    def load_model(self) -> None:
        """
        Loads the model from a specified path, or builds it
        if it doesn't exist.
        """
        model_path = Path(
            f'{model_settings.model_path}/{model_settings.model_name}',
        )

        logger.info(
            f'checking the existence of model config file at {model_path}',
        )

        if not model_path.exists():
            logger.warning(
                f'model at {model_path} not found -> '
                f'building {model_settings.model_name}',
            )
            build_model()

        logger.info(
            f'model {model_settings.model_name} exists! -> '
            f'loading model configuration file',
        )

        with model_path.open('rb') as file:
            self.model = pk.load(file)

    def predict(self, input_parameters: list) -> list:
        """Makes a prediction using the loaded model.

        Takes input parameters and passes it to the model, which
        was loaded using a pickle file.

        Args:
            input_parameters (list): The input data for making the prediction.

        Returns:
            list: The predictions from the model.
        """
        logger.info('making a prediction!')
        return self.model.predict([input_parameters])

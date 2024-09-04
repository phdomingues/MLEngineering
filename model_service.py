# 1. pick up model
    # 1.1. If config file exists, load trained model
    # 1.2. If config file does not exist -> train model to get it
# 2. make predictions

import pickle as pk

from pathlib import Path

from config import settings
from model import build_model
from loguru import logger

class ModelService:
    def __init__(self) -> None:
        self.model = None

    def load_model(self):
        model_path = Path(f'{settings.model_path}/{settings.model_name}')
        logger.info(f"checking the existence of model cinfig file at {model_path}")

        if not model_path.exists():
            logger.warning(f"model at {model_path} not found -> building {settings.model_name}")
            build_model()
        
        logger.info(f"model {settings.model_name} exists! -> loading model configuration file")
        self.model = pk.load(open(f'{settings.model_path}/{settings.model_name}', 'rb'))
    
    def predict(self, input_parameters):
        logger.info("making a prediction!")
        return self.model.predict([input_parameters])
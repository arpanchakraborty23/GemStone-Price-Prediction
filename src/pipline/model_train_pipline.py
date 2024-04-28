from src.configure.config_manager import ConfigManager
from src.logging.logger import logging
from src.exception.exception import CustomException
from src.components.model_train import ModelTrain
import os,sys

STAGE_NAME = "Model Train stage"

class DataIngestionPipline:
    def __init__(self) -> None:
          pass
           
    def pipline(self):
        try:
            config=ConfigManager()
            model_train_config=config.get_model_train_config()
            model_train=ModelTrain(config=model_train_config)
            model_train.initate_model_trainer()
        except CustomException as e:
                    logging.info(f'Error cooured {str(e)}')
                    raise CustomException(sys,e)    
        


if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrain()
        obj.pipline()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e                         
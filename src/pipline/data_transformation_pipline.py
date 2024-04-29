from src.configure.config_manager import ConfigManager
from src.logging.logger import logging
from src.exception.exception import CustomException
import os,sys
from src.components.data_transformation import DataTransformation

STAGE_NAME = "Data Transformation stage"

class DataTransformationPipline:
    def __init__(self) -> None:
        pass

    def pipline(self):
        try:
            config=ConfigManager()
            data_tranformation_config=config.get_data_transformation_config()
            data_tranformation=DataTransformation(config=data_tranformation_config)
            data_tranformation.initiating_data_transformation()
        except Exception as e:
                    logging.info(f'Error cooured {str(e)}')
                    raise CustomException(sys,e) 
                

if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipline()
        obj.pipline()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e                 
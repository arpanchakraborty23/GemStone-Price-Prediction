from src.configure.config_manager import ConfigManager
from src.entity.config_entity import DataIngestionConfig
from src.components.data_ingestion import DataIngestion

from src.logging.logger import logging
from src.exception.exception import CustomException
import os,sys

STAGE_NAME = "Data Ingestion stage"
class DataIngestionPipline:
    def __init__(self) -> None:
          pass
           
    def pipline(self):       
        try:
            logging.info('data ingestion pipline')
            config=ConfigManager()
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion=DataIngestion(config=data_ingestion_config)
            data_ingestion.initiate_data_ingestion()
        except Exception as e:
                    logging.info(f'Error occured {str(e)}')
                    raise CustomException(sys,e)           
        

if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPipline()
        obj.pipline()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e        
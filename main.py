from src.logging.logger import logging
from src.exception.exception import CustomException
from src.pipline.data_ingestion_pipline import DataIngestionPipline



STAGE_NAME = "Data Ingestion stage"
try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPipline()
        obj.pipline()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise e    
from src.logging.logger import logging
from src.exception.exception import CustomException
import os,sys
from src.pipline.data_ingestion_pipline import DataIngestionPipline
from src.pipline.data_transformation_pipline import DataTransformationPipline
from src.pipline.model_train_pipline import ModelTrainPipline
from src.pipline.model_eval_pipline import ModelEvalPipline


STAGE_NAME = "Data Ingestion stage"
if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPipline()
        obj.pipline()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.info('error occured ',str(e)) 

STAGE_NAME = "Data Transformation stage"   
if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipline()
        obj.pipline()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.info('error occured ',str(e))  
        raise CustomException(sys,e)
STAGE_NAME = "Model Train stage"
if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainPipline()
        obj.pipline()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.info('error occured',str(e))
        raise CustomException(sys,e)         
    
# STAGE_NAME = "Model eval stage"
# if __name__ == '__main__':
#     try:
#         logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#         obj = ModelEvalPipline()
#         obj.pipline()
#         logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
#     except Exception as e:
#         logging.info('error occured',str(e))
#         raise CustomException(sys,e) 
import os,sys
from src.configure.config_manager import ConfigManager
from src.logging.logger import logging
from src.exception.exception import CustomException
from src.components.model_eval import ModelEval,ModelEvalConfig

STAGE_NAME = "Model eval stage"

class ModelEvalPipline:
    def __init__(self) -> None:
          pass
           
    def pipline(self):
        try:
            config=ConfigManager()
            model_eval_config=config.get_model_eval_config()
            model_train=ModelEval(config=model_eval_config)
            model_train.initiating_model_eval()
        except CustomException as e:
                    logging.info(f'Error cooured {str(e)}')
                    raise CustomException(sys,e)    
        


if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvalPipline()
        obj.pipline()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e      
import mlflow
import mlflow.sklearn
import os,sys
import numpy as np
import pandas as pd
from urllib.parse import urlparse
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from dotenv import load_dotenv
load_dotenv()

from src.logging.logger import logging
from src.exception.exception import CustomException
from src.utils.utils import save_json,load_obj
from src.configure.config_manager import ModelEvalConfig

class ModelEval:
    def __init__(self,config:ModelEvalConfig) -> None:
        self.config=config

    def eval_metrics(self,y_actual,y_pred):
        try:
            acuracy=r2_score(y_actual,y_pred)*100
            MSE=mean_squared_error(y_actual,y_pred)*100

            MAE=mean_absolute_error(y_actual,y_pred)*100
            RMSE=np.sqrt(MSE)

            return MSE,MAE,RMSE,acuracy
        except Exception as e:
            logging.info('error occured',str(e))
            raise CustomException(sys,e)

    def initiating_model_eval(self):
        try:
            logging.info('model evL has started')

            test_array=np.load(self.config.test_arr)
            model=load_obj(self.config.model)
          

           

            x_test=test_array[:,:-1]
            y_test=test_array[:,-1]

            mlflow_uri=os.getenv('MLFLOW_TRACKING_URI')

            # mlflow.set_registry_uri('https://dagshub.com/arpanchakraborty23/GemStone-Price-Prediction.mlflow')

            track_uri_type_store=urlparse(mlflow.get_tracking_uri()).scheme

            print(track_uri_type_store)

            with mlflow.start_run():
                predict=model.predict(x_test)
                (MSE,MAE,RMSE,acuracy)=self.eval_metrics(y_actual=y_test,y_pred=predict)

                scores={'Rmse':RMSE,'Mse':MSE,'Mae':MAE,'acuracy':acuracy}

                save_json(file_path=self.config.metrics,data=scores)

                mlflow.log_metric('Rmse',RMSE)
                mlflow.log_metric('Mse',MSE)
                mlflow.log_metric('Mae',MAE)
                mlflow.log_metric('acuracy',acuracy)

               
                if track_uri_type_store !='file':
                    mlflow.sklearn.log_model(model,'model',registered_model_name='regressor_model')

                else:
                    mlflow.sklearn.log_model(model,'model')   
                    logging.info('completed model eval')

        except Exception as e:
            logging.info(f' Error occured {str(e)}')
            raise CustomException(sys,e) 





            
from src.utils.utils import save_obj,model_evaluate
from src.logging.logger import logging
from src.exception.exception import CustomException
from src.entity.config_entity import ModelTrainConfig
import os,sys
import numpy as np
from sklearn.linear_model import LinearRegression,Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KDTree



class ModelTrain:
    def __init__(self,config:ModelTrainConfig) -> None:
        self.config=config

    def initate_model_trainer(self):
        try:
            train_array=np.load(self.config.train_arr)
            test_array=np.load(self.config.test_arr)

            x_train, y_train, x_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1])
            models={
                'Liner Regression':LinearRegression(),
                'Ridge Regeassor' : Ridge(),
                'RandomForest Regressor': RandomForestRegressor(),
                'Ada Boost Regressor':AdaBoostRegressor(),
                'DecisionTree Regressor' : DecisionTreeRegressor()
                }
            model_report:dict=model_evaluate(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test,models=models)   
            print( model_report)

            print( model_report)

            
            logging.info(f'Model Report : {model_report}')

            print('\n====================================================================================\n')

            # 6. Find the best model
            best_model_score=max(sorted(model_report.values()))

            
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , Score : {best_model_score}')


            save_obj(
                file_path=self.config.model,
                obj=best_model
            )
            return self.config.model
            
        except CustomException as e:
            logging.info(f'Error cooured {str(e)}')
            raise CustomException(sys,e)    

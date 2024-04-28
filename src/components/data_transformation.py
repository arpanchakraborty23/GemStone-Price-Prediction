from src.utils.utils import save_obj
from src.logging.logger import logging
from src.exception.exception import CustomException
from src.configure.config_manager import DataTransformationConfig

import os,sys
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OrdinalEncoder
from sklearn.impute import SimpleImputer




class DataTransformation:
    def __init__(self,config:DataTransformationConfig) -> None:
        self.config=config
       

    def get_data_transformation_obj(self):
        try:
            num_cols=['carat', 'depth', 'table', 'x', 'y', 'z']
            catagorical_cols=['cut', 'color', 'clarity']

            color_labels=['D', 'E', 'F', 'G', 'H', 'I', 'J']
            cut_labels=['Fair', 'Good', 'Very Good','Premium','Ideal']
            clarity_labels=['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

            logging.info('Pipeline creation started')

            num_cols_pipline=Pipeline(
                steps=[
                    ('IMPUTE',SimpleImputer(strategy='median')),
                    ('SCALING',StandardScaler())
                ]
            )

            catagorical_cols_pipline=Pipeline(
                steps=[
                    ('ODINAL ENCODING',OrdinalEncoder(categories=[cut_labels,color_labels,clarity_labels])),
                    ('IMPUTE',SimpleImputer(strategy='most_frequent')),
                    ('SCALING',StandardScaler())
                ]
            )

            logging.info('pipline created')
            preprocesser_obj=ColumnTransformer(
                [
                    ('num_cols',num_cols_pipline,num_cols),
                    ('categorical_cols',catagorical_cols_pipline,catagorical_cols)
                ]
            )
            logging.info(f'preprocesser object competed {preprocesser_obj}')
            return preprocesser_obj
            
        except CustomException as e:
            logging.info(f'Error cooured {str(e)}')
            raise CustomException(sys,e)   


    def initiating_data_transformation(self):
        try:
            train_data=pd.read_csv(self.config.train_data)
            test_data=pd.read_csv(self.config.test_data)
            

            logging.info('data read completed')

            Target_col=self.config.target_col
           

            logging.info('spliting data x_train,y_tran,x_test,y_test')
            # x_train
            input_feature_train_data=train_data.drop(columns=[Target_col,'Unnamed: 0' ],axis=1)
            print(input_feature_train_data.head())

            # y_train
            target_feature_train_data=train_data[Target_col]
            
            
            #x_test
            input_feature_test_data=test_data.drop(columns=[Target_col,'Unnamed: 0' ],axis=1)

            #y_test
            target_feature_test_data=test_data[Target_col]

            preprocesser=self.get_data_transformation_obj()

            transform_input_feature_train_data=preprocesser.fit_transform(input_feature_train_data)
            transform_input_feature_test_data=preprocesser.transform(input_feature_test_data)

            train_arr=np.c_[transform_input_feature_train_data,np.array(target_feature_train_data)]
            test_arr=np.c_[transform_input_feature_test_data,np.array(target_feature_test_data)]
            
            np.save(self.config.train_arr,train_arr)
            np.save(self.config.test_arr,test_arr)

            save_obj(
                file_path=self.config.preproecss_obj,
                obj=preprocesser
            )

            return(
                train_arr,
                test_arr
            )





        except CustomException as e:
            logging.info(f'Error cooured {str(e)}')
            raise CustomException(sys,e)     
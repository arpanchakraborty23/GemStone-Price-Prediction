import os,sys
import pandas as pd
from src.exception.exception import CustomException
from src.logging.logger import logging
from src.utils.utils import load_obj

class PredictionPipline:
    def __init__(self) -> None:
        logging.info('prediction pipline started')

    def predict(self,feature):
        try:
            preprocesser_obj=load_obj('artifacts\data_transformation\preprocesser.pkl')
            model=load_obj('artifacts\model_trainer\model.pkl')
            logging.info('model loded')
            scale=preprocesser_obj.transform(feature)
            pred=model.predict(scale)

            return pred
        
        except Exception as e:
            logging.info('Error occured',str(e))
            raise CustomException(sys,e)

class CustomData:
    def __init__(self,
                  carat:float,
                 depth:float,
                 table:float,
                 x:float,
                 y:float,
                 z:float,
                 cut:str,
                 color:str,
                 clarity:str) -> None:

        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def get_data_as_df(self):
        try:
            data_input_as_dict={
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]
            }    

            df=pd.DataFrame(data_input_as_dict)
            logging.info('Data Geather')
            return df
        except Exception as e:
            logging.info('Error occured',str(e))
            raise CustomException(sys,e)
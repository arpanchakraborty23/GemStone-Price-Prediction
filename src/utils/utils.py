import os,sys
import yaml
import pickle
import json
import pandas as pd
from pathlib import Path
from pymongo import MongoClient
from box import ConfigBox
from ensure import ensure_annotations
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

from src.logging.logger import logging
from src.exception.exception import CustomException

@ensure_annotations
def read_yaml(file_path:Path):
    try:
        with open(file_path) as y:
            content=yaml.safe_load(y)
            logging.info(f'{file_path} load successfully')

        return ConfigBox(content)    

    except Exception as e:
        raise CustomException(sys,e)
    
@ensure_annotations   
def create_dir(file_path:list,verbose=True):
    try:
        for path in file_path:
            os.makedirs(path,exist_ok=True)
            if verbose:
                logging.info(f"created directory at: {path}")    
    except Exception as e:
        raise CustomException(sys,e)     

def read_data_from_db(db,collection,url):
    client=MongoClient(url)

    db=client[db]
    collection=db[collection]

    data=collection.find()

    df=pd.DataFrame(data=data)
    df.drop('_id',axis=1,inplace=True)
    print(df.head())
    return df

def save_obj(file_path:Path,obj):
    with open(file_path,'wb') as f:
        pickle.dump(obj,f)

def load_obj(file_path):
    with open(file_path,'rb') as f:
        return pickle.load(f)

def model_evaluate(x_train, y_train, x_test, y_test, models):
    try:
        report = {}
        logging.info('model evaluation started')
        
        for i in range(len(models)):
            model = list(models.values())[i]
            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)
            accuracy = r2_score(y_test, y_pred)*100

            logging.info(f'accuracy score for {list(models.keys())[i]}: {accuracy}')
           
            

            # Calculate mean absolute error
            mae = mean_absolute_error(y_test, y_pred)
       

            # Calculate mean squared error
            mse = mean_squared_error(y_test, y_pred)
          
            report[list(models.keys())[i]] =[
                f'Accuracy: {accuracy:.2f}%  MAE: {mae:.2f}%  MSE: {mse:.2f}%'   
            ]

        return report

    except Exception as e:
            logging.info(f'Error in utils {str(e)}')
            raise CustomException(sys,e)            
    
def save_json(file_path,data:dict):
    with open(file_path,'w') as j:
        json.dump(data,j,indent=4)
import os,sys
import yaml
import pandas as pd
from pathlib import Path
from pymongo import MongoClient
from box import ConfigBox
from ensure import ensure_annotations

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
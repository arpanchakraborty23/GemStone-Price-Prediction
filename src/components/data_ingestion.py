import os,sys
from sklearn.model_selection import train_test_split

from src.entity.config_entity import DataIngestionConfig
from src.utils.utils import read_data_from_db
from src.logging.logger import logging
from src.exception.exception import CustomException

from src.utils.utils import read_data_from_db

from dotenv import load_dotenv
load_dotenv()
url=os.getenv('url')
db=os.getenv('db')
collection=os.getenv('collection')

class DataIngestion:
    def __init__(self,config:DataIngestionConfig) -> None:
        self.config=config

    def initiate_data_ingestion(self):
        try:
            logging.info('data ingestion has started')
            df=read_data_from_db(url=url,db=db,collection=collection)

            print(df.head())

            logging.info('data read competed') 
            df.to_csv(self.config.raw_data)

            train_data,test_data=train_test_split(df,test_size=0.26,random_state=0)

            train_data.to_csv(self.config.train_data)

            test_data.to_csv(self.config.test_data)

            logging.info('Data ingestion completed')

            return (
                self.config.test_data,
                self.config.test_data
            )            
        except PermissionError as e:
            logging.info(f'Error cooured {str(e)}')
            raise CustomException(sys,e)        
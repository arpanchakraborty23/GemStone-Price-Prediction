import os,sys
from src.utils.utils import read_yaml,create_dir
from src.entity.config_entity import DataIngestionConfig
from src.constant.ymal_path import *




class ConfigManager:
    def __init__(self,
                 config_file_path=Config_ymal_file_path,
                 prams_file_path=Param_ymal_file_path,
                 schema_file_path=Schema_ymal_file_path) -> None:
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(prams_file_path)
        self.schema=read_yaml(schema_file_path)

        create_dir([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_dir([config.dir])

        data_ingestion_config = DataIngestionConfig(
           dir=config.dir,
           train_data=config.train_data,
           test_data=config.test_data,
           raw_data=config.raw_data
        )

        return data_ingestion_config
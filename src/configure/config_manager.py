import os,sys
from src.utils.utils import read_yaml,create_dir
from src.entity.config_entity import DataIngestionConfig,DataTransformationConfig,ModelTrainConfig,ModelEvalConfig
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
    
    def get_data_transformation_config(self):
          config=self.config.data_transformation
          schema=self.schema.TARGET_COLUMN

          create_dir([config.dir])

          data_transformation_config=DataTransformationConfig(
                dir=config.dir,
                train_data=config.train_data,
                test_data=config.test_data,
                preproecss_obj=config.preproecss_obj,
                target_col=schema.name,
                train_arr=config.train_arr,
                test_arr=config.test_arr
          )
          return data_transformation_config
    
    def get_model_train_config(self):
          config=self.config.model_trainer
          
         

          create_dir([config.dir])

          model_train_config=ModelTrainConfig(
                dir=config.dir,
                train_arr=config.train_arr,
                test_arr=config.test_arr,
                model=config.model
                
          )
          return model_train_config
    def get_model_eval_config(self):
        config=self.config.model_eval
        schema=self.schema.TARGET_COLUMN

        model_eval_config=ModelEvalConfig(
            dir=config.dir,
            test_data=config.test_arr,
            model=config.model,
            metrics=config.metrics,
            Target_col=schema.name
        )
        return model_eval_config
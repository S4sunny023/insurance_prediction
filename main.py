from Insurance.logger import logging
from Insurance.exception import InsuranceException
from Insurance.utils import get_collection_as_dataframe
from Insurance.entity import config_entity
from Insurance.entity.config_entity import DataIngestionConfig

import sys, os

if __name__=="__main__":
     try:
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
     except Exception as e:
          print(e)    
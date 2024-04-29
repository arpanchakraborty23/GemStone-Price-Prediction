from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    dir:Path
    train_data: Path
    test_data: Path
    raw_data : Path


@dataclass
class DataTransformationConfig:
    dir: Path
    train_data: Path
    test_data: Path
    preproecss_obj: Path
    target_col:str
    train_arr:Path
    test_arr: Path

@dataclass
class ModelTrainConfig:
    dir:Path
    train_arr:Path
    test_arr:Path
    model: Path

@dataclass
class ModelEvalConfig:
    dir: Path
    test_arr:Path
    model: Path
   
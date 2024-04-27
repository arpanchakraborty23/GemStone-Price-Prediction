from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    dir:Path
    train_data: Path
    test_data: Path
    raw_data : Path
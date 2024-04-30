# End TO End Gemstone Price Prediction

## Create env
```
conda create -p env python==3.9 -y
conda activate ./env
```
## Install Dependecies
```
pip install -r requirements.txt
```

## Workflow
1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configmanager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the dvc.yaml

## Mldlow Tracking with DagsHub

### Export in Git Bash
```
export MLFLOW_TRACKING_URI=
export MLFLOW_TRACKING_USERNAME=
export MLFLOW_TRACKING_PASSWORD=
```
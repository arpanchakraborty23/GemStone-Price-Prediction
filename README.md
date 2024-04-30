# End TO End Gemstone Price Prediction

## Create env
```
conda create -p env python==3.9 -y
conda activate ./env
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



## create env variable
```
.env

url='mongodb+srv://<username>:<password>@cluster1.kdt4bq1.mongodb.net/'
db=database_name
collection=collection_name


MLFLOW_TRACKING_URI= 
MLFLOW_TRACKING_USERNAME=
MLFLOW_TRACKING_PASSWORD=
```

need to work json file save and model regestry
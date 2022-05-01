# ML pipeline to expose API on Heroku

Udacity project about creating a pipeline to train a model and publish it with a public API on Heroku.

## Developer environment

### Githooks

Flake8 githooks needs to be installed on local development environment with following steps:

* Install precommit binary following https://pre-commit.com/#installation
* Execute `pre-commit install`

## Code/Model testing

Test suite can be executed by `pytest`, including local API test `api_server_test.py`

## EDA notebook

An EDA notebook is available in [EDA](EDA) folder for exploration; same procedures are applied on basic cleaning procedure.

## Procedures

### Basic cleaning procedure

Cleaning data can be done by `python main.py --action basic_cleaning`

### Train/test model procedure

Model training and test ca be dione by `python main.py --action train_test_model`

### Check model score procedure

Check score on latest dvs saved model can be done by `python main.py --action check_score`

### Run entire pipeline

To run the entire pipeline in sequence, use `python main.py --action all` or `python main.py`

### Serve the API on local

If local FastAPI server is needed, execute `uvicorn api_server:app --reload`

### Check Heroku deployed API

Check Heroku deployed API using `python check_heroku_api.py`

## CI/CD

Every step is automated so on Push/Pull Request [Python application](.github/workflows/api_server.yaml) is triggered.
Pipeline pulls data from DVC and execute Flake8 + pytest doing every test.

Unfortunately, CD is not applied due to recent Heroku security breach https://status.heroku.com/incidents/2413

## Repository files

```
workspace
|____screenshots               # screenshots required by project rubric
|
|____EDA                       # EDA process
|
|____data                      # tracked data
|  
|____model                     # tracked model
| 
|____src                       # source code for ML and test python files
| 
|____api_server.py             # create REST API
|
|____api_server_test.py        # REST API test
|
|____check_herou_api.py        # Query live API
|
|____main.py                   # ML pipeline
|
|____model_card.md             # ML model card
|
|____README.md                 # README file
|
|____project_instructions.md   # Project instruction
|
|____retuirements.txt          # Required packages for the environment
|
|____runtime.txt               # Specify python version for deploying heroku
|
|____slice_output.txt          # Model performance on data slicing
|
|____setup.py                  #
|
|____Aptfile                   # For dvc pull
|
|____Procfile                  # For deploying heroku
|
|____setup.py                 # For setup tools

```

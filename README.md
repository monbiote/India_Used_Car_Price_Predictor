# Final Project-Used Car Predicton

This project evaluates multiple machine learning models and finds the best one to predict the prices of second hand cars in India. 

### Installation instructions

To install our library:

( create a virtual environment (conda: conda create --name name_of_environment python 3.12) and activate the environment (conda: conda activate name_of_environment)
- locate your work directory to the library folder "folder_lib" (using terminal: cd path)
- run in terminal "pip install -e." when located in the main library folder.

You should then be able to import the functions from within the library (example: used_car_prediction_lib.data_read.reader, used_car_prediction_lib.data_process.deleteProcessor).


### Library Structure "folder_lib"
```
folder_lib
└─────best_model_prediction
│       └─Predictions.csv (stores the dataset with the predicted values)
└─────used_car_prediction_lib
    └────data_exploration
    │   └───dataExplorer.py
    │   │    └─class RangeDataExplorer
    │   │    └─class NormalityDataExplorer
    │   │    └─class MissingValuesDataExplorer
    │   │    └─class OutliersDataExplorer
    │   │   
    │   └───graphicsExplorer.py
    │        └─class BoxPlotsGraphicsExplorer
    │        └─class DistributionGraphicsExplorer
    │        └─class CorrelationMatrixGraphicsExplorer
    │
    └────data_process
    │   └───deleteProcessor.py
    │   │    └─class DropDeleteProcessor
    │   │   
    │   └───fillProcessor.py
    │        └─class MeanFillProcessor
    │        │   └─def fill
    │        │   └─def handle_outliers_mean
    │        └─class DistributionFillProcessor
    │        │   └─def fill
    │        └─class KNNFillProcessor
    │            └─def fill
    │            └─def handle_outliers_mean
    │
    └────data_read
    │   └───reader.py
    │        └─class CSVReader
    │            └─def read
    │            └─def split_df
    └────features
    │   └───convertor.py
    │   │    └─class StringConvertor
    │   │    │   └─def convert_engine
    │   │    │   └─def convert_kms
    │   │    │   └─def convert_seats
    │   │    │   └─def keep_first_word
    │   │    └─class OwnershipConvertor
    │   │    │   └─def extract_first_integer
    │   │    │   └─def process_ownership
    │   │    └─class PriceUnitConvertor
    │   │        └─def convert_comma_to_dot
    │   │        └─def convert_price
    │   │   
    │   └───encoder.py
    │   │    └─class BinaryEncoder
    │   │    │   └─def encode
    │   │    └─class OneHotEncoder
    │   │        └─def encode
    │   │   
    │   └───transformator.py
    │        └─class Normalization_Transformator
    │        │   └─def transform
    │        └─class Standardization_Transformator
    │        │   └─def transform
    │        └─class Log_Transformator
    │        │   └─def transform
    │        └─class Square_Transformator
    │            └─def transform
    │ 
    └────model
        └───modelCrossValidator.py
        │    └─class Lasso_Regression_ModelCrossValidator
        │    │   └─def train_validate
        │    └─class Ridge_Regression_ModelCrossValidator
        │    │   └─def train_validate
        │    └─class Gradient_Boosting_Regression_ModelCrossValidator
        │        └─def train_validate
        │   
        └───modelSelector.py
        │    └─class ModelSelector
        │        └─def select_best_model
        │        └─def save_predictions_to_csv
        │   
        └───modelTrainer.py
             └─class Linear_Regression_ModelTrainer
             │   └─def train
             └─class Lasso_Regression_ModelTrainer
             │   └─def train
             └─class Ridge_Regression_ModelTrainer
                 └─def train
```

We constructed our whole project using classes that were placed in library structure that made the most sense to us. The objective of this was to create a clear library structure that would allow new collaborators to quickly understand our project and then be able to improve it simply.

This README file birefly summarizes our methodology and motivates the library structure we have build so far, while also showcasing the resul we obtained. 
Finally and most importantly, we also present several suggestion and improvements that could be brought to our project.




we first started by exploring the d



This project is predction of used car

Our project is preparing data, cleaning data and computing data in the end.

We first build function to each operation blocks and remove dupilcation. 
After that, we refactory functions to classes 
and then build entire unittest to make sure the desired behavior.

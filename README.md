# Final Project-Used Car Predicton

This project evaluates multiple machine learning models and finds the best one to predict the prices of second hand cars in India. 

### Installation instructions

To install our library:

( create a virtual environment (using conda: conda create --name name_of_environment python 3.12) and activate the environment (conda: conda activate name_of_environment)
- locate your work directory to the library folder "folder_lib" (using terminal: cd path)
- run in terminal "pip install -e." when located in the main library folder.

You should then be able to import the functions from the library (example: used_car_prediction_lib.data_read.reader, used_car_prediction_lib.data_process.deleteProcessor).

### Library Structure "folder_lib"
```
folder_lib
└─────best_model_prediction
│       └─Predictions.csv (stores a dataset with the predicted values)
└─────used_car_prediction_lib (library)
    └────data_exploration
    │   └───dataExplorer.py
    │   │    └─class RangeDataExplorer
    │   │    │   └─def check
    │   │    └─class NormalityDataExplorer
    │   │    │   └─def check
    │   │    └─class MissingValuesDataExplorer
    │   │    │   └─def check
    │   │    └─class OutliersDataExplorer
    │   │        └─def check
    │   │   
    │   └───graphicsExplorer.py
    │        └─class BoxPlotsGraphicsExplorer
    │        │   └─def plot
    │        └─class DistributionGraphicsExplorer
    │        │   └─def plot
    │        └─class CorrelationMatrixGraphicsExplorer
    │            └─def plot
    │
    └────data_process
    │   └───deleteProcessor.py
    │   │    └─class DropDeleteProcessor
    │   │        └─def delete
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

We constructed our whole project with a library structure that made the most sense to us. The objective was to create a clear library structure that would allow new collaborators to quickly understand our project and then be able to improve it simply.

This README file briefly summarizes our methodology and motivates the library structure we have build so far, while also showcasing the results we obtained. 
Finally and most importantly, we also present several suggestion and improvements that could be brought to our project.

### Summary of the library
- The first folder of our library contains methods that can be used to perform a comprehensive data exploration such as testing the normality of the variable distribution, identifying missing values and outliers and chekcing the range of the variables. It also contains methods to plot correlation matrix, boxplots and distributions.

- The folder data process contains methods that delete variables from the dataset, handle outliers and fill missing values using the distribution, the mean or the k-neirest-neighbor methods. 

- DataRead allows to read and split datasets into train and test. 

- The folder features firstly contains methods to convert variables into numerical values by convertings strings/categorical values into numerical values that can be analyzed. It also contains methods that convert commas into dots or performs scalings. Secondly, it includes methods that transform binary and categorical variables into numerical using respectively a simple 0/1 transformation and a one hot encoder (creating multiple binary variables associated to each category). Finally, it also includes methods used to normalize, standardize, sqaure or perform a logaritm transformation.

- The folder model includes methods that define multiple machine learning models and computes the associated performance metrics to allow a comparison among the different models. Finally it also includes a method that directly compares the models (using the MSE as the comparison metrics) and outputs the name of the best model with its associated MSE and stores the predicted values computed by the most accurate model in the folder "best_model_prediction".

### Pipeline

Our pipeline assemble the preprocessing, the feature engineering and finally the prediction step. 

### Unit Test
Our unit testing is summarized on the following html link: 

### Scaling our library/ Suggestions

We have build our library in a way that would allow new contributers to simply modify and improve our library. In order to modify or improve any methods present in the library, you can simply refer to the schema and the library summary above to identify the location of the methods that you would like to modify. 

Preprocessors: 
- So far we only included 3 imputing methods for the missing values and outliers. Namely, mean, distribution and knn fill. Multiple other imputing methods could be added within the fillprocessor.py file.

Features:
- Other methods could be added to our transformator.py file.

Models/Metrics:
- Multiple other predictions methods could be added to our modelselector.py file using the same strucutre as the other methods already in the file. The models outputs such as the metrics can be easily changed to any other desired performance metrics that is not present.
- If you decide to add or modify any model, please also add the new metrics or new model in the method select_best_model.  


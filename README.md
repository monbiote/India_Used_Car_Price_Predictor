# Final Project-Used Car Predicton
Authors: Luke Atazona, Mathieu Breier, Wu Hangze, Edward Monbiot

This project evaluates multiple machine learning models and finds the best one to predict the prices of second hand cars in India. 

### Installation instructions

To install our library:

( create a virtual environment (using conda: conda create --name name_of_environment python 3.12) and activate the environment (conda: conda activate name_of_environment)
- locate your work directory to the library folder "folder_lib" (using terminal: cd path)
- run in terminal "pip install -e." when located in the main library folder.

You should then be able to import the functions from the library (example: import used_car_prediction_lib.data_read.reader, import used_car_prediction_lib.data_process.deleteProcessor).

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
We designed our entire project based on a library structure that seemed most logical to us. The primary goal was to establish a coherent and comprehensible library structure, ensuring that new contributors could easily understand and enhance it.

This README provides a brief overview of our approach, outlining the rationale behind our current library structure. It also offers recommendations and suggestions for potential enhancements to our project.

### Summary of the library
- Within our library's initial folder, you'll find methods that can be used to perform comprehensive data exploration. These methods encompass various functionalities like assessing variable distribution normality, identifying missing values and outliers, and inspecting variable ranges. Additionally, this section offers tools for visualizing correlation matrices, boxplots, and distributions.

- The data process folder hosts methods dedicated to manipulating datasets. These include procedures for removing variables, handling outliers, and filling missing values using distribution, mean, or k-nearest-neighbor techniques.

- DataRead functionalities enable dataset reading and splitting into training and testing subsets.
  
- The features folder serves a dual purpose. Firstly, it contains methods to convert non-numeric variables into numerical values suitable for analysis, transforming strings or categorical values accordingly. It also offers tools for processing commas to dots and performing scaling operations. Secondly, it includes methods to convert binary and categorical variables into numerical ones, employing a 0/1 transformation and a one-hot encoder, respectively. Additionally, it provides functions for normalization, standardization, squaring, or logarithmic transformations.

- The model folder includes methods defining various machine learning models and computing the associated performance metrics to facilitate model comparison. Lastly, it includes a method that performs a direct model comparison using the Mean Squared Error (MSE) as the evaluation metric and outputs the optimal hyperparameters for each model. This method outputs the best model's name along with its associated MSE. Furthermore, the predicted values generated by the most accurate model are stored in the "best_model_prediction" folder.

### Pipeline

Our pipeline assemble the preprocessing, the feature engineering and finally the prediction step. 

### Scaling our library/ Suggestions

We have build our library in a way that would allow new contributers to simply modify and improve our library. To modify or improve any methods within the library, you can refer to the schema and the library summary provided above to locate the specific methods you wish to modify.

Preprocessors: 
- So far, we have only included 3 imputation methods for handling missing values and outliers: mean, distribution and KNN fill. Various other imputation methods could be added within the fillprocessor.py file.

Features:
- Other methods could be added to our transformator.py file.

Models/Metrics:
- Multiple other predictions methods could be added to our modelselector.py file using the same structure as the other existing methods.The model outputs, such as the metrics, can be easily changed to any other desired performance metric that is not currently available.
- If you decide to add or modify any model, please include the new metrics or/and model within the select_best_model method.

### Results
Linear Regression MSE: 442497139407.946 and RMSE:442497139407.946  with an R2 of 0.641
Lasso Model with Cross Validation MSE: 442518703006.899 and RMSE:665220.793 with an R2 of 0.641 (alpha=31.257)
Ridge Model with Cross Validation MSE: 442931371433.803 and RMSE:665530.894 with an R2 of 0.641 (alpha=0.521))
Gradient Boosting Model with Cross Validation MSE: 232636185273.258 and RMSE:482323.735 with an R2 of 0.811 

### Conclusion
The best model is: Gradient Boosting with an MSE of 232636185273.258, RMSE of 482323.735 and an R2 of 0.811

### Further Improvements

#### Preprocessors
- Explore other imputation methods to be included in the `fillprocessor.py` file.

#### Features
- Expand the techniques used in the `transformator.py` file.

#### Models/Metrics
- Integrate additional predictive methods in the `modelselector.py` file.
- Employ more advanced statistical performance metrics for model evaluation.

#### Pipeline
- Optimize the Python pipeline by encapsulating features to leverage the `sklearn` pipeline technique.
- Develop fitting and transforming methods for improved workflow efficiency.





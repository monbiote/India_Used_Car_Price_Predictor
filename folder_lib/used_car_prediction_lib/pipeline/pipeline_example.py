from ..data_read import reader as rd
from ..features import convertor as cnvrt
class UsedCar_MLPipeline:
    def __init__(self,path,dataHandlingCustomPipeline,modelSelectingCustomPipeline):
        """
        Initialize the pipeline with custom modules for each step of the process.

        :param imputer: Instance of a class derived from FillProcessor for data imputation.
        :param encoder: Instance of a class derived from Encoder for data encoding.
        :param model_selector: Instance of ModelSelector for selecting the best model.
        :param cross_validator: Instance of a class derived from ModelCrossValidator for cross-validation.
        :param model_trainer: Instance of a class derived from ModelTrainer for training the final model.
        """
        self.dataHandlingCustomPipeline = dataHandlingCustomPipeline 
        self.modelSelectingCustomPipeline = modelSelectingCustomPipeline
        self.path = path
        reader = rd.CSVReader()
        self.df = reader.read('car_price.csv')
        self.train_df = None
        self.test_df = None

    def handling_data(self):
        """
        Preprocess the data by imputing and encoding.

        :param X: The input DataFrame.
        :param columns_to_impute: List of columns to impute.
        :param columns_to_encode: List of columns to encode.
        :return: Preprocessed DataFrame.
        """

    def select_and_train_model(self, X_train=None, y_train=None, X_test=None, y_test=None):
        """
        Select the best model, perform cross-validation, and train the model.

        :param X_train: Training feature matrix.
        :param y_train: Training target vector.
        :param X_test: Testing feature matrix.
        :param y_test: Testing target vector.
        """
        # Select best model, cross-validate, and train
        # ...

    def run_pipeline(self, test_size=0.2):
        """
        Run the entire pipeline from preprocessing to model training.

        :param test_size: Fraction of data to be used as test set.
        """

        # Split data into training and testing sets
        # Preprocess data
        # Select, cross-validate, and train model
        # ...


class Custom_MLPipeline:
    def __init__(self):
        """
        Initialize the pipeline with custom modules for each step of the process.
        """

        self.pipeline = []

    def preprocess_data(self, X, columns_to_impute, columns_to_encode):
        """
        Preprocess the data by imputing and encoding.

        :param X: The input DataFrame.
        :param columns_to_impute: List of columns to impute.
        :param columns_to_encode: List of columns to encode.
        :return: Preprocessed DataFrame.
        """
        # Impute and encode data
        # ...

    def select_and_train_model(self, X_train, y_train, X_test, y_test):
        """
        Select the best model, perform cross-validation, and train the model.

        :param X_train: Training feature matrix.
        :param y_train: Training target vector.
        :param X_test: Testing feature matrix.
        :param y_test: Testing target vector.
        """
        # Select best model, cross-validate, and train
        # ...

    def run_pipeline(self, X, y, columns_to_impute, columns_to_encode, test_size=0.2):
        """
        Run the entire pipeline from preprocessing to model training.

        :param X: Feature matrix.
        :param y: Target vector.
        :param columns_to_impute: List of columns to impute.
        :param columns_to_encode: List of columns to encode.
        :param test_size: Fraction of data to be used as test set.
        """
        # Split data into training and testing sets
        # Preprocess data
        # Select, cross-validate, and train model
        # ...

class Custom_MLPipe:
    def __init__(self, pipeName, pipe):
        """
        Initialize the pipeline with custom modules for each step of the process.

        :param pipeName: Name of Pipe.
        :param pipe: Instance of a pipe.
        """
        self.pipeName = pipeName
        self.pipe = pipe

    def getPipe(self):
        """
        Preprocess the data by imputing and encoding.

        :return: Pipe Name and Pipe.
        """
        a =1
        b = [('scaler', a),b[0][1]]
        
        print(type(b[0][0]),'\n',b)
        return (self.pipeName, self.pipe)

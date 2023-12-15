from ..data_read import reader as rd
from ..features import convertor as cnvrt

#########################In Development###############################################
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

        """
        Pipe example:
        a =1
        b = [('scaler', a),b[0][1]]
        
        print(type(b[0][0]),'\n',b)
        return (self.pipeName, self.pipe)
        """
        
class Custom_MLPipeline:
    def __init__(self):
        """
        Initialize the pipeline with custom modules for each step of the process.
        """

        self.pipeline = []

    def preprocess_data(self):
        """
        Preprocess the data by imputing and encoding.

        :return: Preprocessed DataFrame.
        """
        # Impute and encode data
        # ...

    def select_and_train_model(self):
        """
        Select the best model, perform cross-validation, and train the model.
        """
        # Select best model, cross-validate, and train
        # ...

    def run_pipeline(self,test_size=0.2):
        """
        Run the entire pipeline from preprocessing to model training.

        :param test_size: Fraction of data to be used as test set.
        """
        # Split data into training and testing sets
        # Preprocess data
        # Select, cross-validate, and train model
        # ...



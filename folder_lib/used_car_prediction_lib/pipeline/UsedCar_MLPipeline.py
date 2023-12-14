#data read
from ..data_read import reader as rd
import used_car_prediction_lib.data_process.deleteProcessor  as dp
#features
from ..features import convertor as cnvrt
import used_car_prediction_lib.features.encoder as ecod
#preprocess
import used_car_prediction_lib.data_process.fillProcessor as fillPrc
#model selector: select best model, cross validate to train model and make parameter tuning
import used_car_prediction_lib.model.modelSelector as modSlc

#designed for used car machine learning pipeline
class UsedCar_MLPipeline:
    def __init__(self,read_path):
        """
        Initialize the pipeline with custom modules for each step of the process.

        :param imputer: Instance of a class derived from FillProcessor for data imputation.
        :param encoder: Instance of a class derived from Encoder for data encoding.
        :param model_selector: Instance of ModelSelector for selecting the best model.
        :param cross_validator: Instance of a class derived from ModelCrossValidator for cross-validation.
        :param model_trainer: Instance of a class derived from ModelTrainer for training the final model.
        """
        self.read_path = read_path
        reader = rd.CSVReader()
        self.df = reader.read(read_path)
        #X y dataset for train
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test =None

    #featuring and data preprocess
    def data_preprocess_and_featuring(self):
        """
        Preprocess the data by imputing, encoding, filling, deleting, dropping .
        """
        #initiate local df
        df = self.df

        ############################Data Preprocess########################
        dropProcessor = dp.DropDeleteProcessor()
        df = dropProcessor.delete(df, ['Unnamed: 0'])
        ##############################################################
        ########################Feature Engineering ########################
        # Apply the conversion function to the 'price' column
        priceUnit_cnvrt = cnvrt.PriceUnitConvertor()
        df['car_prices_in_rupee'] = df['car_prices_in_rupee'].apply(priceUnit_cnvrt .convert_comma_to_dot)
        df['car_prices_in_rupee'] = df['car_prices_in_rupee'].apply(priceUnit_cnvrt.convert_price)

        # Apply the conversion function to the 'kms_driven' column
        string_cnvrt = cnvrt.StringConvertor()
        df['kms_driven'] = df['kms_driven'].apply(string_cnvrt.convert_kms)

        # Apply the conversion function to the 'engine' column
        df['engine'] = df['engine'].apply(string_cnvrt.convert_engine)

        # Apply the conversion function to the 'seats' column
        df['Seats'] = df['Seats'].apply(string_cnvrt.convert_seats)

        # Keep the first word of the column car
        df['car_name'] = df['car_name'].apply(string_cnvrt.keep_first_word)


        ownerShip_cnvrt = cnvrt.OwnershipConvertor()
        # Call the preprocess_data function to handle the ownership column
        df = ownerShip_cnvrt.process_ownership(df)
        ##############################################################

        ######################Feature Engineering ###########################
        binary_ecod = ecod.BinaryEncoder(true_value='Automatic', false_value='Manual')
        df = binary_ecod.encode(df, ['transmission'])

        oneHot_ecod = ecod.OneHotEncoder()

        # Define the columns to one-hot encode
        columns_to_encode = ['fuel_type', 'car_name']

        # Apply the one_hot_encode function
        df = oneHot_ecod.encode(df, columns_to_encode)
        #######################Data Preprocess#############################
        '''
        import used_car_prediction_lib.data_process.fillProcessor as fi_prc

        mean_fi_prc = fi_prc.MeanFillProcessor()
        mean_fi_prc.fill(df,['colmn'])
        mean_fi_prc.fill(df,'colmn')

        distrbuted_fi_prc = fi_prc.DistributionFillProcessor()
        distrbuted_fi_prc.fill(df,['colmn'])

        knn_fi_prc = fi_prc.KNNFillProcessor()
        knn_fi_prc.fill(df,['colmn'])
        knn_fi_prc.handle_outliers_KNN(df,'colmn')
        df.head()'''

        ######################Feature Engineering #############################

        mean_fillPrc = fillPrc.MeanFillProcessor()
        df = mean_fillPrc.handle_outliers_mean(df, 'car_prices_in_rupee')
        df = mean_fillPrc.handle_outliers_mean(df, 'kms_driven')
        df = mean_fillPrc.handle_outliers_mean(df, 'num_owners')
        ##############################################################
        #rest self df
        self.df = df

    #prepare the train test split before modelling
    def prepare_model(self,test_size = 0.3):
        X = self.df.drop('car_prices_in_rupee', axis = 1) # Selecting independent features 
        y = self.df['car_prices_in_rupee'] # Selecting target variable

        reader = rd.CSVReader()
        self.X_train, self.X_test, self.y_train, self.y_test =reader.split_df(X, y, test_size=test_size, random_state=123)

    #Select the best model, perform cross-validation, parameter tuning, and train the model
    #and download to the local folder
    def select_and_train_model(self):
        """
        Select the best model, perform cross-validation, parameter tuning, and train the model.

        """
        # Select best model, cross-validate, parameter tuning, and train
        modelSelector =  modSlc.ModelSelector()

        modelSelector.select_best_model(self.X_train, self.y_train, self.X_test, self.y_test)

    def run_pipeline(self, test_size=0.3):
        """
        Run the entire pipeline from preprocessing to model training.

        :param test_size: Fraction of data to be used as test set.
        """

        # Split data into training and testing sets
        # Preprocess data
        # Select, cross-validate, and train model
        # ...
        self.data_preprocess_and_featuring()
        self.prepare_model(test_size= test_size)
        self.select_and_train_model()

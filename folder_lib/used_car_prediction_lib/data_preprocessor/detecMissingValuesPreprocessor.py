# Function that detects missing values per columns
#def detect_missing_values(dataframe):
#
#    # Get the total number of missing values in the dataframe
#    missing_values = dataframe.isnull().sum()
#
#    # Return the number of missing values
#    return missing_values
#
##example
#detect_missing_values(df)

from . import preprocessor
class detecMissingValuesProcessor(preprocessor.Preprocessor):
    def preprocess(df, columns=[]):
        
        # Get the total number of missing values in the dataframe
        missing_values = df.isnull().sum()

        # Return the number of missing values
        return missing_values


#from used_car_prediction_lib import detecMissingValuesPreprocessor as dmvpr
#detecMissingValuesProcessor = dmvpr.detecMissingValuesProcessor()
##example
#dmvpr.preprocess(df)
from abc import ABCMeta,abstractmethod
from numpy.random import choice
from numpy import percentile, where , nan
from sklearn.impute import KNNImputer
from pandas import DataFrame

class FillProcessor(metaclass = ABCMeta):

    @abstractmethod
    def fill(self,df, column_name):
        return NotImplementedError



class MeanFillProcessor(FillProcessor):
    def fill(self,df, column_name):
        df[column_name].fillna(df[column_name].mean(), inplace=True)
        return df
    
    # Handle outliers -> replace values with mean
    def handle_outliers_mean(self,df, column_name:str):
        df_copy = df.copy()
        column_data = df_copy[[column_name]].values
        #numpy percentile
        Q1 = percentile(column_data, 10)
        Q3 = percentile(column_data, 90)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        #numpy, where(), nan
        df_copy[column_name] = where((column_data < lower_bound) | (column_data > upper_bound), nan, column_data)
        df_copy[column_name].fillna(df_copy[column_name].mean(), inplace=True)
        return df_copy


class DistributionFillProcessor(FillProcessor):
    def fill(self,df, column_name):
        distribution = df[column_name].dropna()
        missing_count = df[column_name].isnull().sum()
        #use numpy.random.choice
        random_samples = choice(distribution, missing_count)
        df.loc[df[column_name].isnull(), column_name] = random_samples
        return df

class KNNFillProcessor(FillProcessor):
    def __init__(self,neighbors=10):
        super().__init__()
        self.neighbors = neighbors
    
    def fill(self,df, column_name):
        imputer = KNNImputer()
        imputed_data = imputer.fit_transform(df)
        df_temp = DataFrame(imputed_data)
        df_temp.columns = df.columns
        df[column_name] = df_temp[column_name]
        return df
    
    # Handle outliers -> replace values with KNN
    def handle_outliers_KNN(self, df, column_name:str):
        df_copy = df.copy()
        column_data = df_copy[[column_name]].values
        #numpy percentile
        Q1 = percentile(column_data, 10)
        Q3 = percentile(column_data, 90)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        #numpy where(), nan
        df_copy[column_name] = where((column_data < lower_bound) | (column_data > upper_bound), nan, column_data)

        df_copy = self.column_fill_KNN(df_copy, column_name)
        return df_copy
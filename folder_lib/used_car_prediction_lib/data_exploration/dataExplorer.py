from abc import ABCMeta,abstractclassmethod
from scipy.stats import shapiro
from pandas.api.types import is_numeric_dtype

class DataExplorer(metaclass = ABCMeta):

    @abstractclassmethod
    def check(self, df, column_name=[]):
        return NotImplementedError
    
class RangeDataExplorer(DataExplorer):
    def check(self, df, column_name=[]):
        for column in df.select_dtypes(include=['int64', 'float64']).columns:
            min_val = df[column].min()
            max_val = df[column].max()
            print(f"{column}: Min = {min_val}, Max = {max_val}")

class NormalityDataExplorer(DataExplorer):
    def __init__(self, alpha=0.05):
        super.__init__()
        self.alpha = alpha

    def check(self, df, column_name=[]):
         # normality test
        stat, p = shapiro(df)
        result = f'Column "{column_name}" looks Gaussian (fail to reject H0)' if p > self.alpha else f'Column "{column_name}" is not normally distributed (reject H0)'
        interpretation = f'Column "{column_name}": Statistics={stat:.3f}, p={p:.3f}. {result}'
        print(interpretation)

class MissingValuesDataExplorer(DataExplorer):

    def check(self, df, column_name=[]):
        # Get the total number of missing values in the dataframe
        missing_values = df.isnull().sum()

        # Return the number of missing values
        return missing_values


class OutliersDataExplorer (DataExplorer):

    def check(self, df, column_name=[]):
        outliers = {}
        for column in df.columns:
        #pandas.api.types check column type is numeric
            if is_numeric_dtype(df[column]):
                q1 = df[column].quantile(0.10)
                q3 = df[column].quantile(0.90)
                iqr = q3 - q1
                lower_bound = q1 - 1.5 * iqr
                upper_bound = q3 + 1.5 * iqr

                outliers_count = ((df[column] < lower_bound) | (df[column] > upper_bound)).sum()
                outliers[column] = outliers_count

        print("Outliers in each numeric column based on quantiles method:")
        for col, count in outliers.items():
            print(f"Column '{col}': {count} outliers")

        return outliers
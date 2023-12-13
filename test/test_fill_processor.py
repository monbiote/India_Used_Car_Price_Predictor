
import unittest
import pandas as pd
import numpy as np
import fillProcessor as fp

class TestFillProcessor(unittest.TestCase):

    def setUp(self):
        # Setup test data with missing values and outliers
        self.df = pd.DataFrame({
            'col1': [1, np.nan, 3, 4, 100],  # Contains missing value and outlier
            'col2': [2, 3, 4, 5, 6],         # No missing values
            'col3': [np.nan, np.nan, np.nan, 8, 9]  # Mostly missing values
        })
        self.mean_fill_processor = fp.MeanFillProcessor()
        self.distribution_fill_processor = fp.DistributionFillProcessor()
        self.knn_fill_processor = fp.KNNFillProcessor()

    def tearDown(self):
        # Resetting test data
        self.df = None

    # Test methods for MeanFillProcessor
    def test_fill_mean(self):
        filled_df = self.mean_fill_processor.fill(self.df.copy(), 'col1')
        self.assertFalse(filled_df['col1'].isnull().any())
        self.assertNotEqual(filled_df.loc[1, 'col1'], 100)  # Outlier should not affect mean

    def test_handle_outliers_mean(self):
        handled_df = self.mean_fill_processor.handle_outliers_mean(self.df.copy(), 'col1')
        self.assertFalse(handled_df['col1'].isnull().any())
        self.assertNotEqual(handled_df.loc[4, 'col1'], 100)  # Outlier should be replaced

    # Test methods for DistributionFillProcessor
    def test_fill_distribution(self):
        filled_df = self.distribution_fill_processor.fill(self.df.copy(), 'col3')
        self.assertFalse(filled_df['col3'].isnull().any())

    # Test methods for KNNFillProcessor
    def test_fill_knn(self):
        filled_df = self.knn_fill_processor.fill(self.df.copy(), 'col1')
        self.assertFalse(filled_df['col1'].isnull().any())

    def test_handle_outliers_KNN(self):
        handled_df = self.knn_fill_processor.handle_outliers_KNN(self.df.copy(), 'col1')
        self.assertFalse(handled_df['col1'].isnull().any())
        self.assertNotEqual(handled_df.loc[4, 'col1'], 100)  # Outlier should be handled

if __name__ == '__main__':
    unittest.main()

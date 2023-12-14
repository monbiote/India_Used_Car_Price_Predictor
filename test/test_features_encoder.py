#if you want to test within class, import unittest and inheritance from it
import unittest

#pytest test with function start from head of test
import pytest_cov

import pandas as pd
import numpy as np
import used_car_prediction_lib.features.encoder as en

#unittest
# with basic concepts of input and output
#use expected output compare with output from tested function
#assert if is wrong

#########################  Encoder ##################################
class TestEncoder(unittest.TestCase):

    def setUp(self):
        # Setup test data
        self.df = pd.DataFrame({
            'binary_column': ['Yes', 'No', 'Invalid'],
            'categorical_column': ['Cat1', 'Cat2', 'Cat3']
        })
        self.binary_encoder = en.BinaryEncoder(true_value='Yes', false_value='No')
        self.onehot_encoder = en.OneHotEncoder()

    def tearDown(self):
        # Resetting test data
        self.df = None

    
    # Test methods for BinaryEncoder
    def test_binary_encode(self):
        encoded_df = self.binary_encoder.encode(self.df.copy(), ['binary_column'])
        expected_df = self.df.copy()
        expected_df['binary_column'] = expected_df['binary_column'].replace({'Yes': 1, 'No': 0, 'Invalid': None})
        pd.testing.assert_frame_equal(encoded_df, expected_df)

    # Test methods for OneHotEncoder 
    def test_onehot_encode_column_set(self):
        encoded_df = self.onehot_encoder.encode(self.df.copy(), ['categorical_column'])
        expected_df = pd.get_dummies(self.df, columns=['categorical_column'], drop_first=True)
        pd.testing.assert_frame_equal(encoded_df, expected_df)

    
    # Test methods for OneHotEncoder
    def test_onehot_encode_single_column(self):
        encoded_df = self.onehot_encoder.encode(self.df.copy(), ['categorical_column'])
        expected_columns = ['binary_column'] + ['categorical_column_' + cat for cat in sorted(self.df['categorical_column'].unique())[1:]]
        self.assertListEqual(sorted(encoded_df.columns.tolist()), sorted(expected_columns))
        # Verifying the one-hot encoded values
        for col in expected_columns[1:]:
            self.assertTrue(all(encoded_df[col].isin([0, 1])))


if __name__ == '__main__':
    unittest.main()

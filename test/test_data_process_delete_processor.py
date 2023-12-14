#if you want to test within class, import unittest and inheritance from it
import unittest

#pytest test with function start from head of test
import pytest_cov

import pandas as pd
import used_car_prediction_lib.data_process.deleteProcessor as dp

#unittest
# with basic concepts of input and output
#use expected output compare with output from tested function
#assert if is wrong

#########################  DeleteProcessor ##################################
class TestDeleteProcessor(unittest.TestCase):

    def setUp(self):
        # Setup test data
        self.df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': [4, 5, 6],
            'col3': [7, 8, 9]
        })
        self.drop_delete_processor = dp.DropDeleteProcessor()

    def tearDown(self):
        # Resetting test data
        self.df = None

    # Test methods for DropDeleteProcessor
    def test_delete_single_column(self):
        modified_df = self.drop_delete_processor.delete(self.df.copy(), 'col1')
        self.assertNotIn('col1', modified_df.columns)
        self.assertIn('col2', modified_df.columns)
        self.assertIn('col3', modified_df.columns)

    def test_delete_multiple_columns(self):
        modified_df = self.drop_delete_processor.delete(self.df.copy(), ['col1', 'col2'])
        self.assertNotIn('col1', modified_df.columns)
        self.assertNotIn('col2', modified_df.columns)
        self.assertIn('col3', modified_df.columns)

    def test_delete_non_existent_column(self):
        modified_df = self.drop_delete_processor.delete(self.df.copy(), 'non_existent_column')
        self.assertListEqual(sorted(modified_df.columns), sorted(self.df.columns))

if __name__ == '__main__':
    unittest.main()

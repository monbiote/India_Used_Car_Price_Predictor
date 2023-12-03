#if you want to test within class, import unittest and inheritance from it
import unittest

#pytest test with function start from head of test
import pytest_cov

import used_car_prediction_lib.features.transformator as tr


import pandas as pd
import numpy as np
#unittest
# with basic concepts of input and output
#use expected output compare with output from tested function
#assert if is wrong

#########################  Quetion3 ##################################

class TestPlaneFigure_subclasses(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    #instantiate mock object
    def setUp(self):
        print("setup")
        # Creating a sample DataFrame
        data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
        self.df = pd.DataFrame(data)

        self.square_transformator = tr.Square_Transformator()
        self.nromalization_transformator = tr.Square_Transformator()
        
    def tearDown(self):
        print("teardown\n")
        #refresh test variable
        self.square_transformator = tr.Square_Transformator()
        self.nromalization_transformator = tr.Square_Transformator()

    #test Rectangle
    def test_square_transformation(self):
        # Apply your square transformation
        squared_df = self.square_transformator.transform(self.df,['col1','col2'])
        #expected_data = {'col1': [1, 4, 9], 'col2': [16, 25, 36]}
        #expected_df = pd.DataFrame(expected_data)
        expected_df = self.df ** 2

        # Check the shape of the DataFrame
        self.assertEqual(squared_df.shape, expected_df.shape)

        # Check column names
        self.assertListEqual(squared_df.columns.tolist(), ['col1', 'col2'])

        # Check data types
        for dtype in squared_df.dtypes:
            self.assertTrue(dtype in [float, int])

        # Check specific data values
        pd.testing.assert_frame_equal(squared_df, expected_df)

#several files---make sure its our file
if __name__ == '__main__':
    unittest.main()
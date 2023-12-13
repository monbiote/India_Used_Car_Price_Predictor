
import unittest
import pandas as pd
import numpy as np
import convertor as cv

class TestConvertor(unittest.TestCase):

    def setUp(self):
        # Setup test data
        self.df = pd.DataFrame({
            'engine': ['1500 CC', '2000 CC', 'Invalid'],
            'kms': ['10,000 kms', '20,000 kms', 'Invalid'],
            'seats': ['5 Seats', '4 Seats', 'Invalid'],
            'ownership': ['First Owner', 'Second Owner', 'Invalid'],
            'price': ['10 Lakh', '1.5 Crore', 'Invalid']
        })
        self.string_convertor = cv.StringConvertor()
        self.ownership_convertor = cv.OwnershipConvertor()
        self.price_unit_convertor = cv.PriceUnitConvertor()

    def tearDown(self):
        # Resetting test data
        self.df = None

    
    # Test methods for StringConvertor
    def test_convert_engine(self):
        converted = self.df['engine'].apply(self.string_convertor.convert_engine)
        expected = pd.Series([1500.0, 2000.0, None])
        pd.testing.assert_series_equal(converted, expected)

    def test_convert_kms(self):
        converted = self.df['kms'].apply(self.string_convertor.convert_kms)
        expected = pd.Series([10000, 20000, None])
        pd.testing.assert_series_equal(converted, expected)

    def test_convert_seats(self):
        converted = self.df['seats'].apply(self.string_convertor.convert_seats)
        expected = pd.Series([5, 4, None])
        pd.testing.assert_series_equal(converted, expected)

    def test_keep_first_word(self):
        converted = self.df['ownership'].apply(self.string_convertor.keep_first_word)
        expected = pd.Series(['First', 'Second', 'Invalid'])
        pd.testing.assert_series_equal(converted, expected)

    # Test methods for OwnershipConvertor
    def test_extract_first_integer(self):
        converted = self.df['ownership'].apply(self.ownership_convertor.extract_first_integer)
        expected = pd.Series([1, 2, None])
        pd.testing.assert_series_equal(converted, expected)

    def test_process_ownership(self):
        processed_df = self.ownership_convertor.process_ownership(self.df.copy())
        expected_df = self.df.copy()
        expected_df['num_owners'] = pd.Series([1, 2, None])
        expected_df.drop(columns=['ownership'], inplace=True)
        pd.testing.assert_frame_equal(processed_df, expected_df)

    # Test methods for PriceUnitConvertor
    def test_convert_price(self):
        converted = self.df['price'].apply(self.price_unit_convertor.convert_price)
        expected = pd.Series([10.0, 1.5, None])  # Assuming the logic for Lakh and Crore conversion is correctly implemented in convert_price
        pd.testing.assert_series_equal(converted, expected)


    def test_convert_kms(self):
        # Apply the convert_kms method and check results
        pass

    def test_convert_seats(self):
        # Apply the convert_seats method and check results
        pass

    def test_keep_first_word(self):
        # Apply the keep_first_word method and check results
        pass

    # Test methods for OwnershipConvertor
    def test_extract_first_integer(self):
        # Apply the extract_first_integer method and check results
        pass

    def test_process_ownership(self):
        # Apply the process_ownership method and check results
        pass

    # Test methods for PriceUnitConvertor
    def test_convert_price(self):
        # Apply the convert_price method and check results
        pass

if __name__ == '__main__':
    unittest.main()

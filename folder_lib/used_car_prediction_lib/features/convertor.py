class StringConvertor:
    # Remove the string in the engine column
    def convert_engine(column):
        try:
            num_value = float(column.split(" ")[0])
            return num_value
        except ValueError:
            return None
        
    # Remove the string in the power kms_driven
    def convert_kms(column):
        try:
            # Remove commas and 'kms', then convert to integer
            return int(column.replace(',', '').replace(' kms', ''))
        except ValueError:
            return None

    # Remove the string in the Seats column
    def convert_seats(seats_str):
        try:
            return int(seats_str.replace(' Seats', ''))
        except ValueError:
            return None

    # Extract the first word
    def keep_first_word(input_string):
        all_words = input_string.split()
        if all_words:
            return all_words[0]
        else:
            return None

class OwnershipConvertor:
    # Remove the string in the ownership column
    def extract_first_integer(ownership_str):
        try:
            return int(''.join(filter(str.isdigit, ownership_str)))
        except ValueError:
            return None
        
    def process_ownership(self, df):
        # Create a new column 'num_users' by applying the extract_first_integer function
        df['num_owners'] = df['ownership'].apply(self.extract_first_integer)
        
        # Drop the original 'ownership' column
        df.drop(columns=['ownership'], inplace=True)

        return df

class PriceUnitConvertor:
    #Function that converts column with strings to numerical values only
    def convert_comma_to_dot(column):
        try:
            # Replace commas with periods
            column = column.replace(',', '.')

            return column
        except AttributeError:
            return None
        
    def convert_price(column):
        num_value = float(column.split(" ")[0])

        if 'Crore' in column:
            return num_value * 10000000
        elif 'Lakh' in column:
            return num_value * 100000
        else:
            return num_value
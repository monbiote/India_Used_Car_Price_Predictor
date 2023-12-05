from abc import ABCMeta,abstractmethod

class DeleteProcessor(metaclass = ABCMeta):

    @abstractmethod
    def delete(self,df, columns_to_drop):
        return NotImplementedError
    


class DropDeleteProcessor(DeleteProcessor):
    def delete(self,df, columns_to_drop):
        # If a single column name is provided, convert it to a list
        if isinstance(columns_to_drop, str):
            columns_to_drop = [columns_to_drop]

        # Drop the specified columns
        modified_dataframe = df.drop(columns=columns_to_drop, axis=1)

        return modified_dataframe
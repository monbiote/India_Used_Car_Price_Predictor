import preprocessor
class RemoveNaNsRowPreprocessor(preprocessor.Preprocessor):
    def preprocess(train_data, column):
        return train_data.dropna(subset = column)
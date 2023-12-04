from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score


class Train_Model:
    """
    class of model for training and prediction
    """
    # each time construct, increase by 1
    model_Construct_Instance_Counter = 0

    def __init__(self, feature_columns, target_columns, hyperparameters=None):
            
        """
        
        self:
        feature_columns: contains list of features use to train and predict
        target_columns: target column for predictions and then training
        hyperparameters=None: use to configure model with hyperparameters
        """
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.model = RandomForestClassifier(**hyperparameters if hyperparameters else {})

        self.model_Construct_Instance_Counter += 1

    def train(self, train_data):
        """
        Trains the model using the training dataset

        Argument:
        self: model for fit, and feature column metrics and target
        train_data: data for training
        """

        self.model.fit(train_data[self.feature_columns], train_data[self.target_columns])


    def predict(self, test_data):
        """
        provide predictions using the trained data, and returns predicted probabilities 

        Argument:
        self: trained model
        test_data: data for testing prediction
        """
        Feature_test_data = test_data[self.feature_columns]
        return self.model.predict_proba(Feature_test_data)[:,1]

    def accuracy(self,test_data , predict_column):
        """
        Tells us the accuracy of the prediction

        Argument:
        test_data: data for target value and prediction
        predict_column: column's name for prediction
        """
        return roc_auc_score(test_data[self.target_columns], test_data[predict_column])
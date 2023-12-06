from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.metrics import r2_score, mean_squared_error

from abc import ABCMeta, abstractmethod
import numpy as np

####################father################   
class ModelTrainer(metaclass = ABCMeta):
    
    @abstractmethod
    def train(self,X_train, y_train, X_test, y_test):
        return NotImplementedError

####################child################   
class Linear_Regression_ModelTrainer(ModelTrainer):
    
	def train(self,X_train, y_train, X_test, y_test):
		linear = LinearRegression()
		linear.fit(X_train, y_train)
		y_pred = linear.predict(X_test)
		
		# Calculate accuracy
		mse = mean_squared_error(y_test, y_pred)
		rmse = mean_squared_error(y_test, y_pred, squared=False)
		mse_std = np.std(y_test - y_pred)
		r2 = r2_score(y_test, y_pred)   
		return mse, rmse, mse_std, r2, y_pred

class Lasso_Regression_ModelTrainer(ModelTrainer):
    
    def __init__(self, alphas=[0, 1, 2, 3, 4, 5]):
        self.alphas = alphas

    def train(self, X_train, y_train, X_test, y_test):
        lasso = Lasso(alpha=self.alphas)
        lasso.fit(X_train, y_train)
        
        y_pred = lasso.predict(X_test)
            
        # Calculate accuracy
        mse = mean_squared_error(y_test, y_pred)
        rmse = mean_squared_error(y_test, y_pred, squared=False)
        mse_std = np.std(y_test - y_pred)
        r2 = r2_score(y_test, y_pred)
        
        return mse, rmse, mse_std, r2, y_pred

class Ridge_Regression_ModelTrainer(ModelTrainer):
    def __init__(self, alphas=[0.01, 0.5, 0.75, 1, 2]):  # Corrected spacing around the alphas
        self.alphas = alphas
        
    def train(self, X_train, y_train, X_test, y_test):
        ridge = Ridge(alpha=self.alphas) 
        ridge.fit(X_train, y_train)
        
        y_pred = ridge.predict(X_test)
            
        # Calculate accuracy
        mse = mean_squared_error(y_test, y_pred)
        mse_std = np.std(y_test - y_pred)
        r2 = r2_score(y_test, y_pred)
        
        return mse, mse_std, r2, y_pred

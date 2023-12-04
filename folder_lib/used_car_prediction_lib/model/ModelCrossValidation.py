from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.impute import KNNImputer
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression, Lasso, Ridge, LassoCV, RidgeCV
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

from abc import ABCMeta, abstractmethod
import pandas as pd
import numpy as np

####################father################   
class ModelCrossValidator(metaclass = ABCMeta):
    
    @abstractmethod
    def regressing_process_cv(X_train, y_train, X_test, y_test):
        return NotImplementedError

####################child################   
class Lasso_Regression_ModelCrossValidator(ModelCrossValidator):
    
    def __init__(self, cv = 10):
        self.cv = cv

    #Lasso Regression with Cross Validation
    def regressing_process_cv(self, X_train, y_train, X_test, y_test):
        alphas = np.logspace(-4, 4, 100)  # Define a range of alpha values for optimization
        
        lasso_cv = LassoCV(alphas=alphas, cv=self.cv)
        lasso_cv.fit(X_train, y_train)
        
        best_alpha = lasso_cv.alpha_  # Get the optimized alpha
        
        # Train Lasso regression with the best alpha
        lasso = Lasso(alpha=best_alpha)
        lasso.fit(X_train, y_train)
        
        y_pred = lasso.predict(X_test)
        
        mse = mean_squared_error(y_test, y_pred)
        rmse = mean_squared_error(y_test, y_pred, squared=False)
        mse_std = np.std(y_test - y_pred)
        r2 = r2_score(y_test, y_pred)
        
        return mse, rmse, y_pred, r2, best_alpha


####################child################   
class Ridge_Regression_ModelCrossValidator(ModelCrossValidator):
    def __init__(self, cv = 10):
        self.cv = cv

    #Ridge Regression with Cross Validation
    def regressing_process_cv(self, X_train, y_train, X_test,y_test):
        alphas = np.logspace(-4, 4, 100)  # Define a range of alpha values for optimization
        
        ridge_cv = RidgeCV(alphas=alphas, cv=self.cv)
        ridge_cv.fit(X_train, y_train)
        
        best_alpha = ridge_cv.alpha_  # Get the optimized alpha
        
        # Train Ridge regression with the best alpha
        ridge = Ridge(alpha=best_alpha)
        ridge.fit(X_train, y_train)
        
        y_pred = ridge.predict(X_test)
        
        #Calculate accuracy
        mse = mean_squared_error(y_test, y_pred)
        rmse = mean_squared_error(y_test, y_pred, squared=False)
        mse_std = np.std(y_test - y_pred)
        r2 = r2_score(y_test, y_pred)
        
        return mse, rmse, y_pred, r2, best_alpha
    
####################child################   
class Gradient_Boosting_Regression_ModelCrossValidator(ModelCrossValidator):
    def __init__(self, cv = 10):
        self.cv = cv

    #Ridge Regression with Cross Validation
    def regressing_process_cv(self, X_train, y_train, X_test, y_test):
    
        print('This process might take a few minutes.')
        
        param_grid = {
                'n_estimators': [100],
                'learning_rate': [0.05, 0.1],
                'max_depth': [4, 6],
                'min_samples_split': [10, 20],
                'min_samples_leaf': [1,3],
                'subsample': [0.8, 1.0]
            }

        gb_regressor = GradientBoostingRegressor()
        grid_search = GridSearchCV(estimator=gb_regressor, param_grid=param_grid, cv=self.cv, scoring='neg_mean_squared_error', verbose=1, n_jobs=-1)
        
        grid_search.fit(X_train, y_train)
        best_gb_model = grid_search.best_estimator_
        
        y_pred = best_gb_model.predict(X_test)
        
        # Calculate accuracy
        mse = mean_squared_error(y_test, y_pred)
        rmse = mean_squared_error(y_test, y_pred, squared=False)
        mse_std = np.std(y_test - y_pred)
        r2 = r2_score(y_test, y_pred)
        
        # Retrieve best parameters
        best_params = grid_search.best_params_
        
        # Store results in a dictionary
        results = {
            'mse': mse,
            'rmse': rmse,
            'mse_std': mse_std,
            'r2': r2,
            'best_params': best_params,
            'y_pred': y_pred
        }
        
        return mse, rmse, y_pred, r2, best_params


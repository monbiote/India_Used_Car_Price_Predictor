from .modelCrossValidator import Lasso_Regression_ModelCrossValidator, Ridge_Regression_ModelCrossValidator, Gradient_Boosting_Regression_ModelCrossValidator
from .modelTrainer import Linear_Regression_ModelTrainer
import warnings

class ModelSelector:

    # Function that runs every model
    def select_best_model(self,X_train, y_train, X_test, y_test):
        
        # Suppress warnings
        warnings.filterwarnings("ignore")
        
        # Models without Cross Validation
        # Linear Regression
        lr = Linear_Regression_ModelTrainer()
        linear_mse, linear_rmse,_, linear_r2, y_pred = lr.train(X_train, y_train, X_test, y_test)
        print(f"Linear Regression MSE: {linear_mse:.3f} and RMSE:{linear_mse:.3f}  with an R2 of {linear_r2:.3f}")
        
        # Lasso_cv Model
        larcv = Lasso_Regression_ModelCrossValidator()
        lasso_cv_mse, lasso_cv_rmse, y_pred, lasso_cv_r2, best_alpha= larcv.train_validate(X_train, y_train, X_test, y_test)
        print(f"Lasso Model with Cross Validation MSE: {lasso_cv_mse:.3f} and RMSE:{lasso_cv_rmse:.3f} with an R2 of {lasso_cv_r2:.3f} (alpha={best_alpha:.3f})")
        
        # Ridge_cv Model
        rircv = Ridge_Regression_ModelCrossValidator()
        ridge_cv_mse, ridge_cv_rmse,y_pred, ridge_cv_r2, best_alpha = rircv.train_validate(X_train, y_train, X_test, y_test)
        print(f"Ridge Model with Cross Validation MSE: {ridge_cv_mse:.3f} and RMSE:{ridge_cv_rmse:.3f} with an R2 of {ridge_cv_r2:.3f} (alpha={best_alpha:.3f}))")

        # Gboost Model CV
        gbrcv = Gradient_Boosting_Regression_ModelCrossValidator()
        gboost_cv_mse, gboost_cv_rmse, y_pred, gboost_cv_r2, best_params = gbrcv.train_validate(X_train, y_train, X_test, y_test)
        print(f"Gradient Boosting Model with Cross Validation MSE: {gboost_cv_mse:.3f} and RMSE:{gboost_cv_rmse:.3f} with an R2 of {gboost_cv_r2:.3f} (hyperparamaters: {best_params}))")
        
        # Find the best model based on MSE (add more models and more metrics here)
        min_mse = min(linear_mse,lasso_cv_mse,  ridge_cv_mse,gboost_cv_mse)
        min_rmse = min(linear_rmse, lasso_cv_rmse,  ridge_cv_rmse, gboost_cv_rmse)
        min_r2 = min(linear_r2, lasso_cv_r2,  ridge_cv_r2, gboost_cv_r2)

        # Find the best model based on MSE (add more models and more metrics here)
        if min_mse == linear_mse:
            best_model = 'Linear Regression'
            min_rmse = linear_rmse
            min_r2 = linear_r2

        elif min_mse == lasso_cv_mse:
            best_model = 'Lasso'
            min_rmse = lasso_cv_rmse
            min_r2 = lasso_cv_r2

        elif min_mse == ridge_cv_mse:
            best_model = 'Ridge'
            min_rmse = ridge_cv_rmse
            min_r2 = ridge_cv_r2

        elif min_mse == gboost_cv_mse:
            best_model = 'Gradient Boosting'
            min_rmse = gboost_cv_rmse
            min_r2 = gboost_cv_r2

        # Print the best model and its metrics (add more metrics if needed)
        print(f"The best model is: \033[1m\033[3m{best_model} with an MSE of {min_mse:.3f}, RMSE of {min_rmse:.3f} and an R2 of {min_r2:.3f}\033[0m")

        return best_model
    
    

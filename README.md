# Final Project-Used Car Predicton

This project evaluates multiple machine learning models and finds the best one to predict the prices of second hand cars in India. 

### Installation instructions

To install our library:

( create a virtual environment (conda: conda create --name name_of_environment python 3.12) and activate the environment (conda: conda activate name_of_environment)
- locate your work directory to the library folder "folder_lib" (using terminal: cd path)
- run in terminal "pip install -e." when located in the main library folder.

You should then be able to import the functions from within the library (example: used_car_prediction_lib.data_read.reader, used_car_prediction_lib.data_process.deleteProcessor).


# folder_lib

* [best_model_prediction/](./folder_lib/best_model_prediction)
  * [Gradient Boosting_predictions.csv](./folder_lib/best_model_prediction/Gradient Boosting_predictions.csv)
* [used_car_prediction_lib/](./folder_lib/used_car_prediction_lib)
  * [__pycache__/](./folder_lib/used_car_prediction_lib/__pycache__)
    * [__init__.cpython-311.pyc](./folder_lib/used_car_prediction_lib/__pycache__/__init__.cpython-311.pyc)
  * [data_exploration/](./folder_lib/used_car_prediction_lib/data_exploration)
    * [__pycache__/](./folder_lib/used_car_prediction_lib/data_exploration/__pycache__)
      * [__init__.cpython-311.pyc](./folder_lib/used_car_prediction_lib/data_exploration/__pycache__/__init__.cpython-311.pyc)
      * [dataExplorer.cpython-311.pyc](./folder_lib/used_car_prediction_lib/data_exploration/__pycache__/dataExplorer.cpython-311.pyc)
      * [graphicsExplorer.cpython-311.pyc](./folder_lib/used_car_prediction_lib/data_exploration/__pycache__/graphicsExplorer.cpython-311.pyc)
    * [__init__.py](./folder_lib/used_car_prediction_lib/data_exploration/__init__.py)
    * [dataExplorer.py](./folder_lib/used_car_prediction_lib/data_exploration/dataExplorer.py)
    * [graphicsExplorer.py](./folder_lib/used_car_prediction_lib/data_exploration/graphicsExplorer.py)
  * [data_process/](./folder_lib/used_car_prediction_lib/data_process)
    * [__pycache__/](./folder_lib/used_car_prediction_lib/data_process/__pycache__)
      * [__init__.cpython-311.pyc](./folder_lib/used_car_prediction_lib/data_process/__pycache__/__init__.cpython-311.pyc)
      * [deleteProcessor.cpython-311.pyc](./folder_lib/used_car_prediction_lib/data_process/__pycache__/deleteProcessor.cpython-311.pyc)
      * [fillProcessor.cpython-311.pyc](./folder_lib/used_car_prediction_lib/data_process/__pycache__/fillProcessor.cpython-311.pyc)
    * [__init__.py](./folder_lib/used_car_prediction_lib/data_process/__init__.py)
    * [deleteProcessor.py](./folder_lib/used_car_prediction_lib/data_process/deleteProcessor.py)
    * [fillProcessor.py](./folder_lib/used_car_prediction_lib/data_process/fillProcessor.py)
  * [data_read/](./folder_lib/used_car_prediction_lib/data_read)
    * [__pycache__/](./folder_lib/used_car_prediction_lib/data_read/__pycache__)
      * [__init__.cpython-311.pyc](./folder_lib/used_car_prediction_lib/data_read/__pycache__/__init__.cpython-311.pyc)
      * [reader.cpython-311.pyc](./folder_lib/used_car_prediction_lib/data_read/__pycache__/reader.cpython-311.pyc)
    * [__init__.py](./folder_lib/used_car_prediction_lib/data_read/__init__.py)
    * [reader.py](./folder_lib/used_car_prediction_lib/data_read/reader.py)
  * [features/](./folder_lib/used_car_prediction_lib/features)
    * [__pycache__/](./folder_lib/used_car_prediction_lib/features/__pycache__)
      * [__init__.cpython-311.pyc](./folder_lib/used_car_prediction_lib/features/__pycache__/__init__.cpython-311.pyc)
      * [convertor.cpython-311.pyc](./folder_lib/used_car_prediction_lib/features/__pycache__/convertor.cpython-311.pyc)
      * [encoder.cpython-311.pyc](./folder_lib/used_car_prediction_lib/features/__pycache__/encoder.cpython-311.pyc)
    * [__init__.py](./folder_lib/used_car_prediction_lib/features/__init__.py)
    * [convertor.py](./folder_lib/used_car_prediction_lib/features/convertor.py)
    * [encoder.py](./folder_lib/used_car_prediction_lib/features/encoder.py)
    * [transformator.py](./folder_lib/used_car_prediction_lib/features/transformator.py)
  * [model/](./folder_lib/used_car_prediction_lib/model)
    * [__pycache__/](./folder_lib/used_car_prediction_lib/model/__pycache__)
      * [__init__.cpython-311.pyc](./folder_lib/used_car_prediction_lib/model/__pycache__/__init__.cpython-311.pyc)
      * [modelCrossValidator.cpython-311.pyc](./folder_lib/used_car_prediction_lib/model/__pycache__/modelCrossValidator.cpython-311.pyc)
      * [modelSelector.cpython-311.pyc](./folder_lib/used_car_prediction_lib/model/__pycache__/modelSelector.cpython-311.pyc)
      * [modelTrainer.cpython-311.pyc](./folder_lib/used_car_prediction_lib/model/__pycache__/modelTrainer.cpython-311.pyc)
    * [__init__.py](./folder_lib/used_car_prediction_lib/model/__init__.py)
    * [modelCrossValidator.py](./folder_lib/used_car_prediction_lib/model/modelCrossValidator.py)
    * [modelSelector.py](./folder_lib/used_car_prediction_lib/model/modelSelector.py)
    * [modelTrainer.py](./folder_lib/used_car_prediction_lib/model/modelTrainer.py)
  * [__init__.py](./folder_lib/used_car_prediction_lib/__init__.py)
* [used_car_prediction_lib.egg-info/](./folder_lib/used_car_prediction_lib.egg-info)
  * [PKG-INFO](./folder_lib/used_car_prediction_lib.egg-info/PKG-INFO)
  * [SOURCES.txt](./folder_lib/used_car_prediction_lib.egg-info/SOURCES.txt)
  * [dependency_links.txt](./folder_lib/used_car_prediction_lib.egg-info/dependency_links.txt)
  * [requires.txt](./folder_lib/used_car_prediction_lib.egg-info/requires.txt)
  * [top_level.txt](./folder_lib/used_car_prediction_lib.egg-info/top_level.txt)
* [README.md](./folder_lib/README.md)
* [library_structure](./folder_lib/library_structure)
* [requirements.txt](./folder_lib/requirements.txt)
* [setup.cfg](./folder_lib/setup.cfg)
* [setup.py](./folder_lib/setup.py)



We constructed our whole project using classes that were placed in library structure that made the most sense to us. The objective of this was to create a clear library structure that would allow new collaborators to quickly understand our project and then be able to improve it simply.

This README file birefly summarizes our methodology and motivates the library structure we have build so far, while also showcasing the resul we obtained. 
Finally and most importantly, we also present several suggestion and improvements that could be brought to our project.




we first started by exploring the d



This project is predction of used car

Our project is preparing data, cleaning data and computing data in the end.

We first build function to each operation blocks and remove dupilcation. 
After that, we refactory functions to classes 
and then build entire unittest to make sure the desired behavior.

# Library for Used Car Prediction

This library is built for used car prediction. The used car prediction process contains three procedures:
1. Understand Data
2. Clean Data
3. Compute Data

We have deconstructed the related operations and constructed the functions accordingly, also removing duplications.

Then, we refactored functions into classes and followed the **principles from the Computing for Data Science class**.

## Modules
The library consists of the following modules:
- `data_read`
- `data_exploration`
- `data_process`
- `features`
- `model`

## Class Principles
Our class principle: a class is an object that contains functions and attributes. Our classes are like workers; each worker has its own abilities.

### Examples:
- `DataExplorer.check()`
- `DeleteProcessor.delete()`
- `Transformator.transform()`
- `ModelTrainer.train()`

Each worker has similar workers; therefore, we have Father-Child relationships. We also extract similar actions to execute unified functions by applying an abstract class.

### Father-Child Relationships:
- DataExplorer, RangeDataExplorer, NormalityDataExplorer, ...
- DeleteProcessor, DropDeleteProcessor, ...
- Transformator, Normalization_Transformator, Log_Transformator, ...
- ModelTrainer, Linear_Regression_ModelTrainer, Ridge_Regression_ModelTrainer, ...

### Abstract Unified Actions:
- `DataExplorer.check()`
- `DeleteProcessor.delete()`
- `Transformator.transform()`
- `ModelTrainer.train()`

### Specialized Constructors
We use the `__init__` constructor in some cases where a child class requires extra input.

#### Example:
Child class `Ridge_Regression_ModelTrainer`:
```python
def __init__(self, alphas=[0.01, 0.5, 0.75, 1, 2]):
    self.alphas = alphas

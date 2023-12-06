# Libray for used car prediction

 This is library build for used car prediction.
 used car prediction contains 3 procedures.
 understand data-> clean data-> compute data

We therefore destruct the related operations and construct the functions accordingly, also removed duplications.

Then, we refactory functions to classes and followed by <h3>principle from computing for data science class</h3>.
data_read,data_exploration,data_process;features;model;

our class principle: class is an object that contains functions and attributes
our class is workers. workers have own abilities
Examples:
 DataExplorer,DeleteProcessor,Tansformator,Modeltrainer
 DataExplorer.check()
 DeleteProcessor.delete()
 Tansformator.transform()
 Modeltrainer.train()
each worker has own similiar workers: we, therefore, have Father-Child relationships.
and then we extract same actions to execute unified function by appling abstract class.
Examples:
father-child relations:
 DataExplorer,RangeDataExplorer,NormalityDataExplorer,...
 DeleteProcessor,DropDeleteProcessor
 Tansformator,Normalization_Transformator,Log_Transformator
 Modeltrainer,Linear_Regression_ModelTrainer,Ridge_Regression_ModelTrainer
abstract unified actions:
 DataExplorer.check()
 DeleteProcessor.delete()
 Tansformator.transform()
 Modeltrainer.train()

also, we use \__init__ constructor in some cases that child class requires extra input
Examples:
child class Ridge_Regression_ModelTrainer:
\__init__(self, alphas=[0.01, 0.5, 0.75, 1, 2]):  # Corrected spacing around the alphas
        self.alphas = alphas



in the end there will be unittes.

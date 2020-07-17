# PipelineModelBase

Feel free to modify the `ModelBase` class in `__init__.py` or create a new file to inherit it.

Most of the code would go to `predict()` method and `verify_data()` method. the algorithm in this case is stateless and no training parameters to be saved and reloaded, therefore the `predict()` method needs to load firstly the config file to do the setup, then the input data (according to different algorithm options in method paramter) for estimation. Specific steps and logics can be seperated in other private methods, but the `predict()` should be always the one and the only access point (API). Please sepcify different algorithm options (mode) as method parameters if there is.

`verify_data()` method is for data check and data visualization (exploration) before it is used as input for model prediction.

Please add some basic test case with input data file if you feel it is better than a long and boring data format description.

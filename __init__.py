# encoding: utf-8

import pandas as pd


class ModelBase(object):
    """Base class for algorithm integration

    """

    @staticmethod
    def verify_data(cls, df: pd.DataFrame, **param) -> bool:
        """Data verification
        Each `dataset` need to be verified before it is used
        as input for prediction or training (or configuration).
        Status of the dataset will be set as `VERIFIED` or `INVALID`
        according to the return of the method.

        Args:
            df (pandas.DataFrame): pandas loaded datafile

        Returns:
            valid or invalid according to verification logic
        """
        # free to modify key/value names passed by **param
        file_type = param.get('file_type')
        if file_type == 'config':
            return cls.__verify_config_data(df)
        elif file_type == 'input':
            return cls.__verify_input_data(df)

        raise NotImplemented


    @staticmethod
    def __verify_config_data(cls, df: pd.DataFrame) -> bool:

        raise NotImplemented


    @staticmethod
    def __verify_input_data(cls, df: pd.DataFrame) -> bool:

        return NotImplemented


    @staticmethod
    def train_model(cls, df: pd.DataFrame, **param) -> dict:
        """Train (configure) model

        Args:
            df (pandas.DataFrame): training (config) data

        Returns:
            summary of model if necessary (e.g. loss, iteration details, etc.)
        """

        # if there is no training process, just return config
        # details for later prediction usage. everytime the `train_model`
        # method is called, a new record for `model` or `task` is created
        # and saved in database.

        raise NotImplemented


    @staticmethod
    def predict(cls, **param) -> dict:
        """Model prediction

        """

        # real algorithm here

        raise NotImplemented


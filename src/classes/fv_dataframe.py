from __future__ import annotations

import pandas as panda
from pandas import DataFrame
from pandas.io.parsers import TextFileReader


class FVDataFrame:
    file: str = ''
    separator: str = ''
    file_type: str = 'csv'
    dataframe: TextFileReader | DataFrame

    def __init__(self, file, separator=';'):
        """
        Here we define the main variable we'll need later
        :param file: File that contains all the information
        :param separator: separator for csv file
        """
        self.file = file
        self.separator = separator

        self.set_dataframe()

    def set_dataframe(self):
        self.dataframe = panda.read_csv(f"{self.file}", sep=self.separator)

        if len(self.dataframe) == 0:
            raise Exception("This dataframe doesn't contain data.")

    def get_dataframe(self):
        return self.dataframe

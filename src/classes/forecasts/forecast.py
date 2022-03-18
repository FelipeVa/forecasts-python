from pandas import DataFrame


class ForecastInterface:
    dataframe: DataFrame

    def set(self):
        raise Exception("Define a forecast setter before executing it.")

    def get(self):
        return self.dataframe

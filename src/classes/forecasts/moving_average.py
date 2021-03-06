from pandas import DataFrame
from src.classes.forecasts.forecast import ForecastInterface


class MovingAverage(ForecastInterface):
    dataframe: DataFrame
    demand_key: str
    period_key: str
    n: int

    def __init__(self, dataframe: DataFrame, demand_key, period_key, n=1):
        self.dataframe = dataframe
        self.demand_key = demand_key
        self.period_key = period_key
        self.n = n

        self.set()

    def set(self):
        self.dataframe['Moving_average'] = self.dataframe[self.demand_key].rolling(self.n).mean().shift(1)
        self.dataframe['Error'] = self.dataframe[self.demand_key] - self.dataframe['Moving_average']
        self.dataframe['Absolute_Error'] = self.dataframe['Error'].abs()
        self.dataframe['Square_Error'] = pow(self.dataframe['Error'], 2)

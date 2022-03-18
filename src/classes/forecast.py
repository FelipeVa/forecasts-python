from pandas import DataFrame
from src.classes.forecasts.moving_average import MovingAverage
from src.classes.forecasts.simple_exponential_smoothing import SimpleExponentialSmoothing
from src.classes.forecasts.double_exponential_smoothing import DoubleExponentialSmoothing


class Forecast:
    dataframe: DataFrame
    demand_key: str = 'demand'
    period_key: str = 'period'

    def __init__(self, dataframe: DataFrame):
        self.dataframe = dataframe

    def get_moving_average(self, n: int = 1):
        forecast = MovingAverage(self.dataframe, self.demand_key, self.period_key, n)

        return forecast.get()

    def get_simple_exponential_smoothing(self, alpha: float = 1):
        forecast = SimpleExponentialSmoothing(self.dataframe, self.demand_key, self.period_key, alpha)

        return forecast.get()

    def get_double_exponential_smoothing(self, alpha: float = 1, beta: float = 1):
        forecast = DoubleExponentialSmoothing(self.dataframe, self.demand_key, self.period_key, alpha, beta)

        return forecast.get()

    def get_global_indicators(self):
        if not {'Error', 'Absolute_Error'}.issubset(self.dataframe):
            raise Exception("You should first execute a forecast before getting indicators")

        data = dict()
        data['Average_Error'] = self.dataframe['Error'].mean()
        data['Average_Abs_Error'] = self.dataframe['Absolute_Error'].mean()
        data['Average_Square_Error'] = self.dataframe['Square_Error'].mean()
        data['Std_Error'] = self.dataframe['Error'].std()
        data['Std_Abs_Error'] = self.dataframe['Absolute_Error'].std()

        return data

    def set_demand_key(self, key):
        self.demand_key = key

        return self

    def set_period_key(self, key):
        self.period_key = key

        return self

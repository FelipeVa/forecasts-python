from pandas import DataFrame
from src.classes.forecasts.forecast import ForecastInterface


class DoubleExponentialSmoothing(ForecastInterface):
    dataframe: DataFrame
    demand_key: str
    period_key: str
    alpha: float
    beta: float

    def __init__(self, dataframe: DataFrame, demand_key, period_key, alpha=1, beta=1):
        self.dataframe = dataframe
        self.demand_key = demand_key
        self.period_key = period_key
        self.alpha = alpha
        self.beta = beta

        if self.alpha > 1:
            raise Exception(f"Current value of alpha is {self.alpha}, but it can't be higher than 1.")

        if self.beta > 1:
            raise Exception(f"Current value of beta is {self.beta}, but it can't be higher than 1.")

        self.set()

    def set(self):
        self.dataframe['Double_Exponential_Smoothing'] = self.dataframe[self.demand_key]
        self.dataframe['Xp'] = self.dataframe[self.demand_key]
        self.dataframe['T'] = 1

        i = 1
        while i < len(self.dataframe):
            self.dataframe.loc[i, 'T'] = self.beta * (
                    self.dataframe.loc[i - 1, 'Xp'] - self.dataframe.loc[i - 1, 'Xp']) + (1 - self.beta) * (
                                             self.dataframe.loc[i - 1, 'T'])
            self.dataframe.loc[i, 'Xp'] = self.alpha * self.dataframe.loc[i - 1, 'Double_Exponential_Smoothing'] + (
                    1 - self.alpha) * (
                                                  self.dataframe.loc[i - 1, 'Xp'] + self.dataframe.loc[i - 1, 'T'])

            i += 1

        self.dataframe['Double_Exponential_Smoothing'] = round(self.dataframe['Xp'] + self.dataframe['T'], 0)
        self.dataframe['Error'] = self.dataframe[self.demand_key] - self.dataframe['Double_Exponential_Smoothing']
        self.dataframe['Absolute_Error'] = self.dataframe['Error'].abs()
        self.dataframe['Square_Error'] = pow(self.dataframe['Error'], 2)

    def set_beta(self, beta):
        self.beta = beta

        return self

    def set_alpha(self, alpha):
        self.alpha = alpha

        return self

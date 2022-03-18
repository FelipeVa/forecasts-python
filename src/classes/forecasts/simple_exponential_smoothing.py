from pandas import DataFrame


class SimpleExponentialSmoothing:
    dataframe: DataFrame
    demand_key: str
    period_key: str
    alpha: float

    def __init__(self, dataframe: DataFrame, demand_key, period_key, alpha=1):
        self.dataframe = dataframe
        self.demand_key = demand_key
        self.period_key = period_key
        self.alpha = alpha

        if self.alpha > 1:
            raise Exception(f"Current value of alpha is {self.alpha}, but it can't be higher than 1.")

    def get(self):
        self.dataframe['Simple_Exponential_Smoothing'] = self.dataframe[self.demand_key]

        i = 1
        while i < len(self.dataframe):
            self.dataframe.loc[i, 'Simple_Exponential_Smoothing'] = round(
                self.alpha * self.dataframe.loc[i - 1, self.demand_key] + (1 - self.alpha) * self.dataframe.loc[
                    i - 1, 'Simple_Exponential_Smoothing'], 0)
            i += 1

        self.dataframe['Error'] = self.dataframe[self.demand_key] - self.dataframe['Simple_Exponential_Smoothing']
        self.dataframe['Absolute_Error'] = self.dataframe['Error'].abs()
        self.dataframe['Square_Error'] = pow(self.dataframe['Error'], 2)

        return self.dataframe

    def set_alpha(self, alpha):
        self.alpha = alpha

        return self

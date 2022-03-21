from src.classes.fv_dataframe import FVDataFrame
from src.classes.forecast import Forecast
from src.classes.timer import Timer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    timer = Timer()
    timer.set_start()

    n = 1
    bestN = n
    dF1 = FVDataFrame('./data/1.csv')
    fc1 = Forecast(dF1.get_dataframe())
    fc1.get_moving_average(n)

    indicators = fc1.get_global_indicators()
    bestECP = indicators['Average_Square_Error']

    print(f"Initial solution -> n = {n}; ECP = {bestECP}")

    while n <= len(dF1.get_dataframe()):
        fc1.get_moving_average(n)
        indicators = fc1.get_global_indicators()

        # print(f"Solution -> n = {n}; ECP = {indicators['Average_Square_Error']}")

        if indicators['Average_Square_Error'] <= bestECP:
            bestN = n
            bestECP = indicators['Average_Square_Error']

        n += 1

    timer.set_end()
    timer.set_final()

    print(f"Final Solution -> n = {bestN}; ECP = {bestECP}")
    print(f"Total execution time: {timer.get_final()}")


from src.classes.fv_dataframe import FVDataFrame
from src.classes.forecast import Forecast

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dF1 = FVDataFrame('./data/1.csv')
    fc1 = Forecast(dF1.get_dataframe())

    fc1.get_moving_average()
    print(fc1.get_global_indicators())

    fc1.get_simple_exponential_smoothing()
    print(fc1.get_global_indicators())

    fc1.get_double_exponential_smoothing()
    print(fc1.get_global_indicators())

    # horaInicial = datetime.now()
    # alfa = 0
    # dfP = pronostico.obtener_demanda()
    # dfP = pronostico.obtener_suav_exp_simple(dfP, alfa)
    # indicadores = pronostico.obtener_indicadores_globales(dfP)
    # bestAlfa = alfa
    # bestECP = indicadores['errorCuadPromedio']
    # print(f"Solucion inicial -> alfa = {alfa}; ECP = {bestECP}")
    #
    # while indicadores['errorCuadPromedio'] <= bestECP:
    #     dfP = pronostico.obtener_demanda()
    #     dfP = pronostico.obtener_suav_exp_simple(dfP, alfa)
    #     indicadores = pronostico.obtener_indicadores_globales(dfP)
    #
    #     if indicadores['errorCuadPromedio'] <= bestECP:
    #         bestAlfa = alfa
    #         bestECP = indicadores['errorCuadPromedio']
    #
    #     # print(f"Solucion -> alfa = {alfa}; ECP = {indicadores['errorCuadPromedio']}")
    #
    #     alfa = round(alfa + 0.01, 2)
    # horaFinal = datetime.now()
    # tiempoFinal = horaFinal - horaInicial
    # print(f"Solucion final -> alfa = {bestAlfa}; ECP = {bestECP}")
    # print(f"Tiempo de computo: {tiempoFinal}")
    #
    # horaInicial = datetime.now()
    # # print("************************* PRONOSTICOS *************************")
    # # indicadores = pronostico.obtener_indicadores_globales(dfP)
    # #
    # n = 1
    # dfP = pronostico.obtener_demanda()
    # dfP = pronostico.obtener_promedio_movil(dfP, n)
    # indicadores = pronostico.obtener_indicadores_globales(dfP)
    # bestN = n
    # bestECP = indicadores['errorCuadPromedio']
    #
    # print(f"Solucion inicial -> n = {n}; ECP = {bestECP}")
    # # pronostico.imprimir_indicadores_globales(indicadores)
    # # CICLO con numero de elementos del vecindario
    #
    # while n <= 200:
    #     dfP = pronostico.obtener_demanda()
    #     dfP = pronostico.obtener_promedio_movil(dfP, n)
    #     indicadores = pronostico.obtener_indicadores_globales(dfP)
    #
    #     # print(f"Solucion -> n = {n}; ECP = {bestECP}")
    #
    #     if indicadores['errorCuadPromedio'] <= bestECP:
    #         bestN = n
    #         bestECP = indicadores['errorCuadPromedio']
    #
    #     n += 1
    # horaFinal = datetime.now()
    # tiempoFinal = horaFinal - horaInicial
    # print(f"Solucion final -> n = {bestN}; ECP = {bestECP}")
    # print(f"Tiempo de computo: {tiempoFinal}")

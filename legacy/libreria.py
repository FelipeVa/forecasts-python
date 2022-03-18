import tkinter
import pandas as pd
import matplotlib.pyplot as plt


def obtener_demanda():
    df = pd.read_csv("../data/datos2.csv", sep=";")
    return df


def obtener_promedio_movil(df, n):
    df['promedio_movil'] = df['demanda'].rolling(n).mean().shift(1)

    df['Error'] = df['demanda'] - df['promedio_movil']
    df['Error_Absoluto'] = df['Error'].abs()
    df['Error_Cuadratico'] = pow(df['Error'], 2)
    return df


def obtener_indicadores_globales(df):
    data = dict()
    data['errorPromedio'] = df['Error'].mean()
    data['errorAbsPromedio'] = df['Error_Absoluto'].mean()
    data['errorCuadPromedio'] = df['Error_Cuadratico'].mean()
    data['desvEstError'] = df['Error'].std()
    data['desvEstErrorAbs'] = df['Error_Absoluto'].std()
    data['df'] = df

    return data


def imprimir_indicadores_globales(data):
    print("============= INDICADORES DEL MODELO DE PRONOSTICO =============")
    print(f"Error Promedio = {data['errorPromedio']}")
    print(f"Error Absoluto Promedio = {data['errorAbsPromedio']}")
    print(f"Error Cuadratico Promedio = {data['errorCuadPromedio']}")
    print(f"Desviacion Estandar Error = {data['desvEstError']}")
    print(f"Desviacion Estandar Error Absoluto = {data['desvEstErrorAbs']}")
    # print(data['df'])
    print()


def obtener_grafica(df, columnaPronostico):
    ax = plt.gca()
    df.plot(kind='line', x='periodo', y='demanda', ax=ax)
    df.plot(kind='line', x='periodo', y=columnaPronostico, ax=ax)
    # plt.show()
    plt.savefig("gráfica.png")
    return


def obtener_suav_exp_simple(df, alfa):
    df['suavExpSimple'] = df['demanda']

    i = 1
    while i < len(df):
        df.loc[i, 'suavExpSimple'] = round(
            alfa * df.loc[i - 1, 'demanda'] + (1 - alfa) * df.loc[i - 1, 'suavExpSimple'], 0)
        i += 1

    # Columnas calculo error
    df['Error'] = df['demanda'] - df['suavExpSimple']
    df['Error_Absoluto'] = df['Error'].abs()
    df['Error_Cuadratico'] = pow(df['Error'], 2)

    return df


def obtener_suav_exp_doble(df, alfa, beta):
    df['suavExpDoble'] = df['demanda']
    df['Xp'] = df['demanda']
    df['T'] = 1

    i = 1
    while i < len(df):
        df.loc[i, 'T'] = beta * (df.loc[i - 1, 'Xp'] - df.loc[i - 1, 'Xp']) + (1 - beta) * (df.loc[i - 1, 'T'])
        df.loc[i, 'Xp'] = alfa * df.loc[i - 1, 'suavExpDoble'] + (1 - alfa) * (df.loc[i - 1, 'Xp'] + df.loc[i - 1, 'T'])

        i += 1

    df['suavExpDoble'] = round(df['Xp'] + df['T'], 0)
    # Columnas calculo error
    df['Error'] = df['demanda'] - df['suavExpDoble']
    df['Error_Absoluto'] = df['Error'].abs()
    df['Error_Cuadratico'] = pow(df['Error'], 2)

    return df


def obtener_grafica1(df, columnaPronostico):
    # Grafica
    # gca stands for 'get current axis'
    ax = plt.gca()
    df.plot(kind='line', x='periodo', y='demanda', ax=ax)
    df.plot(kind='line', x='periodo', y=columnaPronostico, color='red', ax=ax)
    plt.show()
    return


def obtener_suavizacion_expo_simple1(df, alfa):
    df['suavExpSimple'] = df['demanda']

    i = 1
    while i < len(df):
        df.loc[i, 'suavExpSimple'] = round(
            alfa * df.loc[i - 1, 'demanda'] + (1 - alfa) * df.loc[i - 1, 'suavExpSimple'], 0)
        i += 1

    df['Error'] = df['demanda'] - df['suavExpSimple']
    df['Error_Absoluto'] = df['Error'].abs()
    df['Error_Cuadratico'] = pow(df['Error'], 2)
    return df


def obtener_suavizacion_expo_doble1(df, alfa, beta):
    df['suavExpDoble'] = df['demanda']
    df['X'] = df['demanda']
    df['T'] = 2

    i = 1
    while i < len(df):
        df.loc[i, 'X'] = round(
            alfa * df.loc[i - 1, 'suavExpDoble'] + (1 - alfa) * (df.loc[i - 1, 'X'] + df.loc[i - 1, 'T']), 0)
        df.loc[i, 'T'] = round(beta * (df.loc[i, 'X'] - df.loc[i - 1, 'X']) + (1 - beta) * df.loc[i - 1, 'T'], 0)

        i += 1

    df['suavExpDoble'] = round(df['X'] + df['T'], 0)
    df['Error'] = df['demanda'] - df['suavExpDoble']
    df['Error_Absoluto'] = df['Error'].abs()
    df['Error_Cuadratico'] = pow(df['Error'], 2)
    return df


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    """
    """

    #Lee archivos de entrada para clima y producto
    file_in = 'MXM00076680.csv'
    df_wt = pd.read_csv(file_in)
    df_wt['date']=pd.to_datetime(df_wt['date'],format='%Y-%m-%d') #Convierte Date de string a datetime

    file_in = 'Producto_agencia_20139.csv'
    df_prod = pd.read_csv(file_in)
    df_prod['fecha']=pd.to_datetime(df_prod['fecha'],format='%Y-%m-%d') #Convierte Date de string a datetime


    #print(np.unique(df_prod['codigo_producto']))     # Print route ids.
    group_cols = ['codigo_producto', 'fecha']
    gk_prod = df_prod.groupby(group_cols, axis='rows')     # Group dataframe by route
    print(gk_prod.head(10))

    T_prom = df_wt['tavg']
    vta_rt = gk_prod['venta_total_piezas'].agg(np.mean)    # Average sales per route
    dev_rt = gk_prod['venta_total_pesos'].agg(np.mean)    # Average devs per route

    # Plot of averaeg devolutions vs sales, per route. A 1st glimpse to the data
    # sugests two kinds of routes: one where the number of sales is significantly
    # higher than the number of devolutions (below the imaginary red line) and
    # another group where the difference between sales and devolutions is not
    # as big (above the red line).
    fig = plt.figure(figsize=(10, 8))
    plt.scatter(vta_rt, dev_rt, alpha=0.8)
    plt.plot([10, 100], [0, 7], c='r')      # Imaginary line to separate clusters.
    plt.xlabel('Avg temp per day')
    plt.ylabel('Product')
    plt.savefig('Product_vs_Temp.png')
    plt.show()
    plt.close('all')

    exit(0)

    # A simmylar analysis can be done by grouping the data per date, instead of
    # route. The interpretation of this 2nd analysis is not as straightforward
    # but still can be interesting to look ad at.


if __name__ == '__main__':
    main()

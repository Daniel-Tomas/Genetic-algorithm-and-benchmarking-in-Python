import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
import matplotlib.colors as col

dataframe = pd.read_csv("data.csv", index_col="Size")

if __name__ == '__main__':
    # print(dataframe.head(5))
    # fig,ax =plt.subplots()
    # # ax.bar(dataframe.index,dataframe['Probabilistic'])
    # #     # ax.bar(dataframe.index,dataframe['Brute Force'])
    # #     # ax.bar(dataframe.index,dataframe['Radix Sort'])
    # #     # ax.bar(dataframe.index,dataframe['Quick Sort'])
    # #     # plt.show()
    # ax.hist(dataframe,105, histtype='bar')
    # fig.tight_layout()
    # plt.show()
    plt.rcParams.update({
        "lines.color": "white",
        "patch.edgecolor": "white",
        "text.color": "white",
        "axes.facecolor": "#121111",
        "axes.edgecolor": "lightgray",
        "axes.labelcolor": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "grid.color": "lightgray",
        "figure.facecolor": "#121111",
        "figure.edgecolor": "black",
        "savefig.facecolor": "#121111",
        "savefig.edgecolor": "black"})

    muestra = dataframe[:].copy()
    # muestra.append(dataframe[-1:].copy())
    muestra.plot(kind='bar', width=0.3);
    plt.xlabel('Size of input (n)', fontsize=16)
    plt.ylabel('Milliseconds', fontsize=16)
    plt.legend(fontsize='large', framealpha=0.6)

    
    plt.xticks(rotation=0)
    plt.yticks(np.arange(0, 2501, 250))

    plt.savefig('grafica_barras.png')
    plt.show()

    # print(col.to_hex("indigo"))
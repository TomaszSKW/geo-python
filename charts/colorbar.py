import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
import seaborn as sns
from matplotlib.colors import Colormap, ListedColormap
#from os import path
#outpath = r"C:\Users\user\Desktop\chyba_wazne\Zuza\python_kodzik\wykresy\colorbar_155"

def create_colorbar(df_hours, df, liczbadni):
    for day in df_hours['data'].unique():
        df_hours_day = df_hours[df_hours['data'] == day]

        dwuwymiar = []  # Lista, która będzie przechowywać puste listy
        for i in range(24):
            new_list = []  # Tworzenie nowej pustej listy
            dwuwymiar.append(new_list)  # Dodawanie nowej pustej listy do listy lists
        q = 0
        qq = 0
        while q <= liczbadni-1:
            while qq <= 23:
                dwuwymiar[qq].append(df_hours['czestotliwosc[Hz]'][qq+q*24])
                qq += 1
            qq = 0
            q += 1

        cmap = plot.cm.jet
        cmap.set_bad(color='gray', alpha=0.3)
        plot.imshow(dwuwymiar, cmap='Blues', interpolation='none')
    plot.colorbar()
    if 1 in df['miesiac'].values:
        plot.title('Styczeń')
        plot.gca().set_xticks(list(range(1, 32)))
    elif 2 in df['miesiac'].values:
        plot.title('Luty')
        plot.gca().set_xticks(list(range(1, 30)))
    elif 3 in df['miesiac'].values:
        plot.title('Marzec')
        plot.gca().set_xticks(list(range(1, 32)))
    # elif 4 in df['miesiac'].values:
    #     plot.title('Kwiecień')
    #     new_x = list(range(1, 31))
    # elif 5 in df['miesiac'].values:
    #     plot.title('Maj')
    #     new_x = list(range(1, 32))
    # elif 6 in df['miesiac'].values:
    #     plot.title('Czerwiec')
    #     new_x = list(range(1, 31))
    # elif 7 in df['miesiac'].values:
    #     plot.title('Lipiec')
    #     new_x = list(range(1, 32))
    # elif 8 in df['miesiac'].values:
    #     plot.title('Sierpień')
    #     new_x = list(range(1, 31))
    # elif 9 in df['miesiac'].values:
    #     plot.title('Wrzesień')
    #     new_x = list(range(1, 31))
    # elif 10 in df['miesiac'].values:
    #     plot.title('Październik')
    #     new_x = list(range(1, 32))
    # elif 11 in df['miesiac'].values:
    #     plot.title('Listopad')
    #     new_x = list(range(1, 31))
    # elif 12 in df['miesiac'].values:
    #     plot.title('Grudzień')
    #     new_x = list(range(1, 32))
    # plot.gca().set_xticks(new_x)   # Aktualizacja wartości osi x na wykresie
    plot.xlabel('Dzień')
    plot.ylabel('Godzina')    
    #plot.savefig(path.join(outpath, "colorbar155_{0}.png".format(day)))
    plot.show()
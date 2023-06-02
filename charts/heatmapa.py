import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
import seaborn as sns
from matplotlib.colors import Colormap, ListedColormap

def create_heatmap(df):
    df_hours_heatmap = df.groupby(by = ['godzina', 'data']).mean(numeric_only=True)['residua'].unstack()
    plot.figure(figsize = (10,7))
    sns.heatmap(df_hours_heatmap, cmap = 'coolwarm')
    if 1 in df['miesiac'].values:
        plot.title('Styczeń')
    elif 2 in df['miesiac'].values:
        plot.title('Luty')
    elif 3 in df['miesiac'].values:
        plot.title('Marzec')
    elif 4 in df['miesiac'].values:
        plot.title('Kwiecień')
    elif 5 in df['miesiac'].values:
        plot.title('Maj')
    elif 6 in df['miesiac'].values:
        plot.title('Czerwiec')
    elif 7 in df['miesiac'].values:
        plot.title('Lipiec')
    elif 8 in df['miesiac'].values:
        plot.title('Sierpień')
    elif 9 in df['miesiac'].values:
        plot.title('Wrzesień')
    elif 10 in df['miesiac'].values:
        plot.title('Październik')
    elif 11 in df['miesiac'].values:
        plot.title('Listopad')
    elif 12 in df['miesiac'].values:
        plot.title('Grudzień')
    new_x = [val + 1 for val in df_hours_heatmap]   # Zaktualizowanie wartości osi x
    plot.gca().set_xticks(new_x)   # Aktualizacja wartości osi x na wykresie
    plot.show()

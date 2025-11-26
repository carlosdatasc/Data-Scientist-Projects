

import matplotlib.pyplot as plt
import seaborn as sns


def data_report(df):

    # Información general
    print("Información general:\n")
    print(df.info())
    print("\n")

    # Resumen estadístico
    print("Resumen estadístico:\n")
    print(df.describe())
    print("\n")

    # Valores nulos
    print("Valores nulos:\n")
    print(df.isnull().sum())
    print("\n")

    # Valores únicos
    print("Valores únicos:\n")
    for col in df.columns:
        print(col, ":", df[col].nunique())
    print("\n")

    # Valores repetidos
    print("Valores repetidos:\n")
    print(df.duplicated().sum())
    print("\n")

def boxplot(df_num):
    #boxplot
    plt.figure(figsize=(8,6))
    sns.set(style='whitegrid')
    colors = sns.color_palette('pastel')

    ax=sns.boxplot(data=df_num, palette=colors)
    ax.set(xlabel='Variables', title=f'Distribución de {df_num}')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

    plt.show()

def countplot(df_cat):
    #countplot
    plt.figure(figsize=(12,6))
    for i in df_cat:
        sns.countplot(x=i, data=df_cat)
        plt.title('Categoricas')
        plt.xlabel('Nada')

        plt.show()

def histograma(df_num):
    sns.set(style='whitegrid')
    for i in df_num:

        plt.figure(figsize=(12,6))

        sns.histplot(df[i], bins=30, color='blue')
        plt.show()


class EDA:
    def __init__(self, df, num, cat, binary, target):
        self.df = df
        self.num = num
        self.cat = cat
        self.binary = binary
        self.target = target
        self.generate_plots()

    def generate_plots(self):
        for i in self.num:
            plt.figure(figsize=(30,10))
            sns.boxplot(x=self.df[i])
            plt.title(i)
            plt.xlabel('Range ' + i)

        for i in self.cat:
            plt.figure(figsize=(30,10))
            sns.countplot(x=self.df[i])
            plt.title(i)
            plt.xlabel('Range ' + i)

        for i in self.num:
            if self.df[i].dtype in ['int64', 'float64'] and len(self.df[i].unique()) > 1:
                plt.figure(figsize=(30,10))
                sns.violinplot(x=self.target, y=i, data=self.df)
                plt.title(f'Violin Plot de {i}')
                plt.xlabel(i)
                plt.ylabel(self.target)
                plt.show()


        for i in self.binary:
            plt.figure(figsize=(30,10))
            sns.countplot(x=self.df[i])
            plt.title(i)
            plt.xlabel('Range ' + i)
            plt.show()
            print(self.df[i].value_counts())
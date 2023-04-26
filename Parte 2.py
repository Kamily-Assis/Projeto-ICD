# -*- coding: utf-8 -*-
"""Projeto1_ICD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FvVvBPMJAoMKoZx1rYSUU7e7s0JRFKTf

#Projeto: Análise Exploratória de Dados de Câncer

##02 - Projeto - Exploração inicial

Objetivo
Na segunda etapa do projeto, vocês efetuarão uma análise exploratória inicial
dos dados.


Tarefas
1. Criar um Jupyter Notebook para iniciar a exploração dos conjuntos de
dados
2. No notebook, calcular medidas de centralidade e dispersão das variáveis
disponíveis
3. No notebook, criar boxplots para as variáveis disponíveis
Entrega
O notebook deve ser acrescentado ao repositório do GitHub do projeto.

Grupo:

Adriel Ferreira

Jéssica Nagahama

Kamily Assis
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

"""**DNS** = "*Deaths for Neoplasms for both Sex*" (Mortes por câncer para ambos os sexos)

"""

df = pd.read_csv('/content/drive/MyDrive/Projeto ICD/cancer-death-rates-by-age.csv')

df = df.rename(columns={ "Deaths - Neoplasms - Sex: Both - Age: Under 5 (Rate)": "| DNS < 5 |",
                "Deaths - Neoplasms - Sex: Both - Age: Age-standardized (Rate)": "DNS Padronizado",
                "Deaths - Neoplasms - Sex: Both - Age: All Ages (Rate)": "| DNS all ages |",
                "Deaths - Neoplasms - Sex: Both - Age: 70+ years (Rate)" : "DNS > 70",
                "Deaths - Neoplasms - Sex: Both - Age: 5-14 years (Rate)" : "| 5 > DNS > 14 |",
                "Deaths - Neoplasms - Sex: Both - Age: 50-69 years (Rate)" : "50 > DNS > 50",
                "Deaths - Neoplasms - Sex: Both - Age: 15-49 years (Rate)" : "| 15 > DNS > 49 |" })

df.head().style.set_table_styles([dict(selector='th', props=[('text-align', 'center')]),
                                    dict(selector='td', props=[('text-align', 'center')])])

"""##Média, Mediana e Moda"""

import scipy.stats as stats
#iterando colunas
for col in df.columns[3:]:
  #checando se as colunas contém valores númericos
  if df[col].dtype != 'object':
    mean = df[col].mean()
    median = df[col].median()
    mode = stats.mode(df[col], keepdims=True)[0][0]
  
    print(f"{col}\n Média: {mean}\n Mediana: {median}\n Moda: {mode}\n")

"""##Variância e Desvio Padrão"""

for col in df.columns[3:]:
  if df[col].dtype != 'object':
    variance = df[col].var()
    std_dev = df[col].std()

    print(f"{col}\n Variância: {variance}\n Desvio Padrão: {std_dev}\n")

"""##Boxplots

Boxplots criados utilizando algumas variáveis do dataset.
"""

df_filtered = df.loc[((df['Year'] == 1990) | (df['Year'] == 2010))]
sns.boxplot(data=df_filtered,x='Year',y='15 > DNS > 49')
plt.title('Taxa de mortalidade (pessoas de 15 à 49 anos) em 1990 e 2010',fontsize=11)

df_filtered_brics = df.loc[((df['Entity'] == 'Brazil') | (df['Entity'] == 'Russia' ) | (df['Entity'] == 'India') | (df['Entity'] == 'China') | (df['Entity'] == 'South Africa'))]
sns.boxplot(data=df_filtered_brics , x='Entity', y='DNS all ages')
plt.title('Taxa de mortalidade (pessoas de todas as idades) dos países do BRICS',fontsize=10)

df_filtered_ukr = df.loc[(df['Entity']=='Ukraine')|(df['Entity'] == 'Russia')]
sns.boxplot(data=df_filtered_ukr , x='Entity', y='DNS all ages',palette="Set1")
plt.title('Taxa de mortalidade (todas as idades) - Ucrânia e Rússia')

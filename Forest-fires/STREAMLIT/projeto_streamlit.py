import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('Análise de Dados')

st.markdown('---')
st.markdown('#  > Casos em cada Estado <')

dados = pd.read_csv('./amazon.csv', sep = ',', header=[0], )

dados.columns = ['Ano', 'Estado', 'Mês', 'N_Queimadas', 'Data']
dados = dados.replace({'Estado': {'Rio': np.nan}}) 
dados['Estado'].fillna('Rio de Janeiro', inplace=True)
plt.rcParams['figure.figsize'] = (18,8)

queimadas_estado = dados.groupby('Estado') ['N_Queimadas'].mean()

queimadas_estado.plot(linestyle='--', color='black', marker='s')
queimadas_estado.plot.bar(edgecolor='black', grid=True, linewidth=1.5)

plt.ylim(0, 250)
plt.ylabel('Casos de Incêndio')
plt.title('Números de Casos por Estado', fontsize = 18)
plt.legend(loc='best')

st.pyplot(plt)

plt.clf()

st.markdown('---')
st.markdown('#  > Casos por Ano <')

queimadas_ano = dados.groupby('Ano') ['N_Queimadas'].mean()

m_e = [6,8,8,8,12,13,12,11,10,10,9,12,11,10,12,10,12,12,13,12]

queimadas_ano.plot.barh(edgecolor='black', color='c', width=0.7, xerr=m_e, capsize=5, ecolor='gray')

plt.xlim(0, 160)
plt.title('Números de Casos por Ano', fontsize= 18)
plt.xlabel('Casos de Incêndio')
plt.legend()

st.pyplot(plt)

plt.clf()

st.markdown('---')
st.markdown('#  > Casos por Mês <')

queimadas_mes = dados.groupby('Mês') ['N_Queimadas'].mean()

explode = (0, 0.2, 0, 0, 0, 0.2, 0.1, 0, 0, 0, 0.1, 0.1)
cores = ['steelblue', 'Gold', 'darkorchid', 'm', 'orange', 'green', 'Dodgerblue', 'lightgreen', 'cyan', 'purple', 'Salmon', 'r']

queimadas_mes.plot.pie(explode=explode, shadow=True, autopct='%1.1f%%', startangle=180, colors=cores)

plt.title('Número de Casos por Mês', fontsize=18)
plt.legend(fontsize=15)
plt.axis('equal')

st.pyplot(plt)

plt.clf()
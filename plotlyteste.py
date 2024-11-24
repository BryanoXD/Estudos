import streamlit as st
import pandas as pd
import plotly.express as px

#teste com plotly para plotar gráficos e montar um dashboard
##comando no cmd para rotar o streamlit que monta o dashboard em servidor local
#streamlit run c:/caminho/Estudos/Planilhas/plotlyteste.py (nomedoarquivo.py)

tabela = pd.read_excel(r'C:\Users\bryan\Documents\Estudos\Planilhas\Produtos.xlsx')

tipo = st.sidebar.selectbox("Tipo:", tabela['Tipo'].unique())

#definindo grid do dashboard
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

#filtrando de acordo com a documentação do plotly
tipo_filtrado = tabela[tabela["Tipo"] == tipo]

graf_produto = px.bar(tipo_filtrado, x="Produtos", y="Preço Base Reais", title="Faturamento por dia")
col1.plotly_chart(graf_produto, use_container_width=True)
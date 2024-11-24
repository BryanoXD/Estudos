import streamlit as st
import pandas as pd
import plotly.express as px

tabela = pd.read_excel(r'C:\Users\bryan\Documents\Estudos\Planilhas\Produtos.xlsx')

tipo = st.sidebar.selectbox("Tipo:", tabela['Tipo'].unique())

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

tipo_filtrado = tabela[tabela["Tipo"] == tipo]

graf_produto = px.bar(tipo_filtrado, x="Produtos", y="Preço Base Reais", title="Faturamento por dia")
col1.plotly_chart(graf_produto, use_container_width=True)

#graf_servico = px.bar(tipo_filtrado, x="Produtos", y="Preço Base Reais", title="Faturamento por tipo de produto", orientation="h")
#col2.plotly_chart(graf_produto, use_container_width=True)
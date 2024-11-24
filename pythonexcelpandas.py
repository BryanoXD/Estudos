import pandas as pd

#teste com pandas

#ler planilha
tabela = pd.read_excel("Planilhas/Produtos.xlsx")
tabela.loc[tabela["Tipo"] == "Serviço", "Multiplicador Imposto"] = 1.5
tabela["Preço Base Reais"] = tabela["Multiplicador Imposto"] * tabela["Preço Base Original"]

#salvar planilha
tabela.to_excel("Planilhas/ProdutosPandas.xlsx", index=False)
tabela2 = pd.read_excel("Planilhas/ProdutosPandas.xlsx")
print(tabela2)
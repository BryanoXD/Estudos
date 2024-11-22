import pandas as pd

tabela = pd.read_excel("Planilhas/Produtos.xlsx")
print(tabela)
tabela.loc[tabela["Tipo"] == "Serviço", "Multiplicador Imposto"] = 1.5
tabela["Preço Base Reais"] = tabela["Multiplicador Imposto"] * tabela["Preço Base Original"]
tabela.to_excel("Planilhas/ProdutosPandas.xlsx", index=False)
tabela2 = pd.read_excel("Planilhas/ProdutosPandas.xlsx")
print(tabela2)
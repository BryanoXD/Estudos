from openpyxl import Workbook, load_workbook

#teste com openpyxl

#ler a planilha
planilha = load_workbook("Planilhas/Produtos.xlsx")

aba_ativa = planilha.active
aba_ativa["C"]

for celula in aba_ativa["C"]:
    if celula.value == "Serviço":
        linha = celula.row
        aba_ativa[f"D{linha}"] = 1.5

planilha.save("Planilhas/ProdutosOpenPy.xlsx")
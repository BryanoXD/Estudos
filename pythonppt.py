from pptx import Presentation

apresentacao = Presentation()

#editar o ppt 
slide1 = apresentacao.slides.add_slide(apresentacao.slide_layouts[0]) # slide com titulo e subtitulo
#slide1 = apresentacao.slides.add_slide(apresentacao.slide_layouts[6]) # slide em branco

titulo = slide1.shapes.title 
subtitulo = slide1.placeholders[1]

titulo.text = "1º Slide do Bryan"
subtitulo.text = "Teste de slide"

#salvar esse ppt
apresentacao.save("Apresentacoes/Apresentacao1.pptx")

#criar PPT personalizados

from pptx import Presentation
from pptx.util import Inches, Pt

apresentacao = Presentation()

slide = apresentacao.slides.add_slide(apresentacao.slide_layouts[6])

x = Inches(1)
y = Inches(1)
largura = Inches(2)
altura = Inches(2)
caixa_texto = slide.shapes.add_textbox(x, y, largura, altura)

#editar uma caixa de texto
caixa_texto.text = "Vendas de Janeiro"

#criar parágrafos
text_frame = caixa_texto.text_frame
paragrafo = text_frame.add_paragraph()
paragrafo.text = "R$10.000"
paragrafo.font.bold = True
paragrafo.font.size = Pt(30)

paragrafo = text_frame.add_paragraph()
paragrafo.text = "Produto mais vendido: IPhone"

#salvar
apresentacao.save("Apresentacoes/Apresentacao2.pptx")


#criar PPTs com Gráficos
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE

apresentacao = Presentation()

slide = apresentacao.slides.add_slide(apresentacao.slide_layouts[6])

#criar gráfico
produtos = ["IPhone", "IPad", "Airpod"] # categorias (eixo x)
vendas = [1500, 1000, 2000] # serie de dados (eixo y)

x = Inches(1)
y = Inches(1)
largura = Inches(5)
altura = Inches(3)

dados_grafico = CategoryChartData()
dados_grafico.categories = produtos
dados_grafico.add_series("Vendas", vendas)
slide.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, x, y, largura, altura, dados_grafico)

apresentacao.save("Apresentacoes/Apresentacao3.pptx")




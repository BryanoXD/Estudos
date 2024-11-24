import requests
from tkinter import *


#teste para abrir janela em desktop com o tkinter
#teste para receber uma api da internet
def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    #transformar json objeto python
    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''
    texto_orientacao["text"] = texto
    
#abrir janela
#.mainloop() mantém a janela aberta
janela = Tk()

botao = Button(janela, text="teste", command=pegar_cotacoes)
botao.grid(column=0, row=1)
texto_orientacao = Label(janela, text="")
texto_orientacao.grid(column=0, row=2)

janela.mainloop()
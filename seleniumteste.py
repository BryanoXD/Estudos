from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#abrir navegador .navegador()
driver = webdriver.Chrome()

#simula uma espera
driver.implicitly_wait(2)

#entra num site
driver.get('https://buscape.com.br')

#encontrar elemento especifico pelo caminho dele
driver.find_element('xpath', '//*[@id="new-header"]/div[1]/div/div/div[3]/div/div/div[2]/div/div[1]/input').send_keys('Galaxy S23' + Keys.ENTER)

driver.maximize_window()

driver.find_element('id', 'orderBy').click()
driver.find_element('xpath', '//*[@id="orderBy"]/option[2]').click()

#pausar o código para visualizar, também posso utilizar para safe pauses
time.sleep(10)
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep



urlPrefeitura = 'https://nfe.prefeitura.sp.gov.br/login.aspx'
urlGuiaIss = 'https://zeus.jettax.com.br/calls?page=1&status&level=2'


## abrir o navegador e acessar a prefeitura
browser = Firefox()
browser.get(urlPrefeitura)


## colocar o login
login = browser.find_element(By.XPATH, '//*[@id="ctl00_body_tbCpfCnpj"]')
login.send_keys(123123123)


##colocar a senha
senha = browser.find_element(By.XPATH, '//*[@id="ctl00_body_tbSenha"]')
senha.send_keys(123)

sleep(5)
browser.close()
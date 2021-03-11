import time
import schedule
import json
import locale
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from django.apps import AppConfig
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teste.settings')
django.setup()
locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')

start_urls = [
    'https://www.kabum.com.br/hardware/placa-de-video-vga/nvidia?pagina=1&ordem=5&limite=100&prime=false&marcas=[]&tipo_produto=[]&filtro=[]',
    'https://www.kabum.com.br/hardware/placa-de-video-vga/nvidia?pagina=2&ordem=5&limite=100&prime=false&marcas=[]&tipo_produto=[]&filtro=[]',
    'https://www.kabum.com.br/hardware/processadores?pagina=1&ordem=5&limite=100&prime=false&marcas=[]&tipo_produto=[]&filtro=[]',
    'https://www.kabum.com.br/hardware/processadores?pagina=2&ordem=5&limite=100&prime=false&marcas=[]&tipo_produto=[]&filtro=[]',
]

options = Options()
options.add_argument("--headless")
options.add_argument("--log-level=3")
options.add_argument("--window-size=1920x1080")
options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36")

if os.path.exists("kabum.json"):
    os.remove("kabum.json")
else:
    print('Kabum não existia')

total = 0
driver = webdriver.Chrome(options=options,
                          executable_path='C:\\Users\\belch\\Desktop\\Backup Códigos\\GPU_site\\teste\\chromedriver.exe')  # Webdriver abre
                          
for url in start_urls:
    driver.get(url)
    produtos = driver.find_elements_by_class_name('sc-fzqNqU.jmuOAh')
    for produto in produtos:
        comparador = produto.find_element_by_css_selector(
            '.dghWOt img').get_attribute('src')
        if comparador == 'https://static.kabum.com.br/conteudo/temas/001/imagens/icones/comprar.png':
            total = total+1
driver.close()


print(total)
driver = webdriver.Chrome(options=options,
                          executable_path='C:\\bin\\chromedriver.exe')  # Webdriver abre
with open('kabum.json', 'a') as file:
    file.write("[")
    file.close()
linha = 0
for url in start_urls:
    driver.get(url)
    produtos = driver.find_elements_by_class_name('sc-fzqNqU.jmuOAh')
    for produto in produtos:
        comparador = produto.find_element_by_css_selector(
            '.dghWOt img').get_attribute('src')
        if comparador == 'https://static.kabum.com.br/conteudo/temas/001/imagens/icones/comprar.png':
            # Preço boleto
            temp_price = produto.find_element_by_class_name('qatGF').text
            ValueToFloat = locale.atof(temp_price.strip("R$"))
            # Preço real
            temp_price_real = produto.find_element_by_class_name('ksiZrQ').text
            RealToFloat = locale.atof(temp_price_real.strip("R$"))

            dicionario = {
                'title': produto.find_element_by_class_name('item-nome').text,
                'price_boleto': ValueToFloat,
                'realprice': RealToFloat,
                'img_link': produto.find_element_by_css_selector('.jmuOAh img').get_attribute('src'),
                'item_link': produto.find_element_by_css_selector('.jmuOAh a').get_attribute('href'),
            }
            with open('kabum.json', 'a') as file:
                linha = linha+1
                file.write(json.dumps(dicionario))
                if linha == total:
                    file.write("\n")
                    file.write("]")
                else:
                    file.write(",")
                    file.write("\n")
            file.close()
        else:
            pass
driver.quit()
os.system('pichau_spider.py')

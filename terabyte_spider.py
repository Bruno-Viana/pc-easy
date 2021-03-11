import time
import schedule
import json
import locale
import re
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from django.apps import AppConfig
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teste.settings')
django.setup()

locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument(
    '--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.302"')

if os.path.exists("terabyte.json"):
    os.remove("terabyte.json")
else:
    print('Terabyte não existia')
with open('terabyte.json', 'a') as file:
    file.write("[")
    file.close()
linha = 0

start_urls = [
    'https://www.terabyteshop.com.br/hardware/placas-de-video',
    'https://www.terabyteshop.com.br/hardware/processadores',
]


#Verifica total
temp_total=0
total = 0
for url in start_urls:
    driver = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path='C:\\bin\\chromedriver.exe')  # Webdriver abre
    time.sleep(1)
    driver.get(url)

    produtos = driver.find_elements_by_css_selector(
        'div.pbox.col-xs-12.col-sm-6.col-md-3')
    esgotados = driver.find_elements_by_class_name('tbt_esgotado')
    total = len(produtos) - len(esgotados)
    temp_total = temp_total + total
    driver.quit()

print("Total tera:" , temp_total)


for url in start_urls:
    driver = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path='C:\\bin\\chromedriver.exe')  # Webdriver abre
    time.sleep(1)
    driver.get(url)

    produtos = driver.find_elements_by_css_selector(
        'div.pbox.col-xs-12.col-sm-6.col-md-3')
    '''esgotados = driver.find_elements_by_class_name('tbt_esgotado')
    total = len(produtos) - len(esgotados)'''
    for produto in produtos:
        # Se produto estiver esgotado, ignore
        if produto.find_elements_by_class_name('tbt_esgotado'):
            None
        else:
            if produto.find_element_by_class_name('prod-new-price').text:
                price_boleto = produto.find_element_by_class_name(
                    'prod-new-price').text
                price_boleto = re.findall("\d+", price_boleto)
                Pos = ''.join(map(str, price_boleto))[-2:]
                Antes = ''.join(map(str, price_boleto))[:-2]
                Valor_final = (Antes+'.'+Pos)
                ValueToFloat = float(Valor_final)

            # Preço real, tratamento
            if produto.find_element_by_class_name('prod-juros').text:
                realprice = produto.find_element_by_class_name(
                    'prod-juros').text
                realprice = re.findall("\d+", realprice)
                formatado = ''.join(map(str, realprice))[2:]
                Pos = ''.join(map(str, formatado))[-2:]
                Antes = ''.join(map(str, formatado))[:-2]
                Valor_final = (Antes+'.'+Pos)
                RealToFloat = float(Valor_final)
                RealToFloat = round((RealToFloat*12), 2)

            dicionario = {
                'title': produto.find_element_by_class_name('prod-name').text,
                'price_boleto': ValueToFloat,
                'realprice': RealToFloat,
                'img_link': produto.find_element_by_css_selector('a.commerce_columns_item_image img').get_attribute('src'),
                'item_link': produto.find_element_by_class_name('prod-name').get_attribute('href'),
            }
            with open('terabyte.json', 'a') as file:
                linha = linha+1
                file.write(json.dumps(dicionario))
                if linha == temp_total:
                    file.write("\n")
                else:
                    file.write(",")
                    file.write("\n")

                file.close()
    driver.quit()
with open('terabyte.json', 'a') as file:
    file.write("]")
    file.close()
    # time.sleep(60) #Vai ser executado a cada x segundos

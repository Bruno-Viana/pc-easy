import time
import schedule
import re
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
    'https://www.pichau.com.br/hardware/placa-de-video?p=1&product_list_limit=48',
    'https://www.pichau.com.br/hardware/placa-de-video?p=2&product_list_limit=48',
    'https://www.pichau.com.br/hardware/processadores?p=1&product_list_limit=48',
]

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1")

if os.path.exists("pichau.json"):
    os.remove("pichau.json")
else:
    print('Pichau não existia')
total = 0

driver = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path='C:\\bin\\chromedriver.exe')  # Webdriver abre
for url in start_urls:
    driver.get(url)
    produtos = driver.find_elements_by_css_selector('li.product-item')
    for produto in produtos:
        try:
            produto.find_element_by_class_name('price-boleto span')
            total = total+1
        except:
            pass

driver.close()


print('Total Pichau:', total)
driver = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path='C:\\bin\\chromedriver.exe')   # Webdriver abre
with open('pichau.json', 'a') as file:
    file.write("[")
    file.close()
linha = 0
for url in start_urls:
    driver.get(url)
    produtos = driver.find_elements_by_css_selector('li.product-item')
    for produto in produtos:
        try:
            # Boleto
            temp_price = re.findall(
                r'\d+', produto.find_element_by_class_name('price-boleto span').text)
            Pos = ''.join(map(str, temp_price))[-2:]
            Antes = ''.join(map(str, temp_price))[:-2]
            Valor_final = (Antes+'.'+Pos)
            ValueToFloat = float(Valor_final)
            # RealPrice
            RealToFloat = float(produto.find_element_by_css_selector(
                '.price-wrapper').get_attribute('data-price-amount'))

            dicionario = {
                'title': produto.find_element_by_css_selector('.product-item-photo img').get_attribute('alt'),
                'price_boleto': ValueToFloat,
                'realprice': RealToFloat,
                'img_link': produto.find_element_by_css_selector('.product-item-photo img').get_attribute('src'),
                'item_link': produto.find_element_by_css_selector('.product-item-link').get_attribute('href'),
            }
            with open('pichau.json', 'a') as file:
                linha = linha+1
                file.write(json.dumps(dicionario))
                if linha == total:
                    file.write("\n")
                    file.write("]")
                else:
                    file.write(",")
                    file.write("\n")
            file.close()
        except:
            pass
driver.quit()
# time.sleep(19080) #Vai começar os crawlers de novo depois de x segundos
os.system('terabyte_spider.py')

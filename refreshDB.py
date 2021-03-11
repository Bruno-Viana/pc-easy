import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "teste.settings")

import django
django.setup()

from django.core.management import call_command
import json
import time
import schedule
from GPU.models import Produto
from django.apps import AppConfig



def refresher():

    print('Começando Import')
    if Produto.objects.all().exists():
        print('Database contém:', len(Produto.objects.all()), )
        Produto.objects.all().delete()

    with open("terabyte.json", "r") as read_file:
        data = json.load(read_file)
        for produto in data:
            ProdtoDB = Produto(nome=produto['title'], price_boleto=produto['price_boleto'],
                               realprice=produto['realprice'], img_url=produto['img_link'], prod_url=produto['item_link'])
            ProdtoDB.save()
            time.sleep(0.1)
        read_file.close()
        
    with open("pichau.json", "r") as read_file:
        data = json.load(read_file)
        for produto in data:
            ProdtoDB = Produto(nome=produto['title'], price_boleto=produto['price_boleto'],
                               realprice=produto['realprice'], img_url=produto['img_link'], prod_url=produto['item_link'])
            ProdtoDB.save()
            time.sleep(0.1)
        read_file.close()
    with open("kabum.json", "r") as read_file:
        data = json.load(read_file)
        for produto in data:
            ProdtoDB = Produto(nome=produto['title'], price_boleto=produto['price_boleto'],
                               realprice=produto['realprice'], img_url=produto['img_link'], prod_url=produto['item_link'])
            ProdtoDB.save()
            time.sleep(0.1)
        read_file.close()
    print('DB Atualizado', len(Produto.objects.all()))


schedule.every().day.at("06:30").do(refresher)
#schedule.every(10).seconds.do(refresher)
while True:
    schedule.run_pending()
    time.sleep(1)

import time
import schedule
from django.apps import AppConfig
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teste.settings')
django.setup()


def getData():
    os.system('kabum_spider.py')


# schedule.every(5).seconds.do(getData)
schedule.every().day.at("06:00").do(getData)
while True:
    schedule.run_pending()
    time.sleep(1)

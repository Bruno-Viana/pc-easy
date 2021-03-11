from selenium.webdriver.chrome.options import Options
from selenium import webdriver



chrome_options = Options()
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1")


driver = webdriver.Chrome(options=chrome_options,
                          executable_path='C:\\bin\\chromedriver.exe')
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from connect import Connect
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('excludeSwitches', ['enable-logging'])
siteSircon = "https://app.sistemasircon.com.br/login"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get(siteSircon)
connect = Connect(driver=driver)


table = pd.read_csv("table.csv", sep=',', encoding='latin_1', dtype=str)
connect.tables = table
table = connect.renameColumn

# print(table)
table.to_csv("table2.csv", index=False, header=True)
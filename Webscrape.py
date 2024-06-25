import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless if you don't need a browser UI
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Ensure the path to your chromedriver is correct
service = Service('chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)
pages = 50

##interando por todas as paginas do site
for i in range(1,pages,1):
    ##Obtendo o HTML
    url = f'https://www.foxterciaimobiliaria.com.br/imoveis/a-venda/em-porto-alegre-rs?page={i}'
    driver.get(url)
    time.sleep(3)
# Send a GET request to the URL
    response = requests.get(url,headers={'Cache-Control': 'no-cache'})
# Check if the request was successful
    if response.status_code == 200:
        print(f'Successfully fetched page {i}')
        # Print the fetched URL and a snippet of the content for debugging
        print(f'URL: {url}')
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        prices = soup.find_all('h1', class_="font-bold text-xl text-foxter-brand-700")
        adress = soup.find_all('div', class_="flex text-sm justify-start text-foxter-brand-900")
        # Contém quartos, banheiros e vagas abaixo:
        m_squared = soup.find_all('span', class_="whitespace-nowrap text-foxter-brand-900")
        code = soup.find_all('div', class_="text-xs text-slate-500 cursor-pointer")    
    else:
        print("Error")
        # Print the response content as text
        #print(response.text)

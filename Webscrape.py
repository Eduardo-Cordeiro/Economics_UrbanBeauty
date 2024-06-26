import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

# Set up Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless if you don't need a browser UI
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Ensure the path to your chromedriver is correct
service = Service('chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

pages = 4

# Info Lists
prices_list = []
street_list = []
neighborhood_list = []
m_squared_list = []
code_list = []


##interando por todas as paginas do site
for i in range(1,pages,1):
    ##Obtendo o HTML
    url = f'https://www.foxterciaimobiliaria.com.br/imoveis/a-venda/em-porto-alegre-rs?page={i}'
    driver.get(url)
    time.sleep(2)
# Send a GET request to the URL
    response = requests.get(url,headers={'Cache-Control': 'no-cache'})
# Check if the request was successful
    if response.status_code == 200:
        print(f'Successfully fetched page {i}')
        # Print the fetched URL and a snippet of the content for debugging
        print(f'URL: {url}')
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        prices = soup.find_all('h1', class_="font-bold text-xl text-foxter-brand-700")
        for p in prices:
            string_price = str(p)
            price = []
            for char in string_price:
                if char.isdigit():
                    price.append(str(char))
            joined = ''.join(price[4:-1])
            prices_list.append(int(joined)/100)
        
        adress = soup.find_all('div', class_="flex text-sm justify-start text-foxter-brand-900")
        for a in adress:
            string_adress = str(a)
            if i == 1:
                street = string_adress.split('>')[1].split('<')[0]
                street_list.append(street)

                if len(string_adress.split('>')) == 3:
                    neighborhood = string_adress.split('>')[1].split(',')[1]
                else:
                    neighborhood = string_adress.split('>')[3].split('<')[0]
                neighborhood_list.append(neighborhood)
            else:
                street = string_adress.split('>')[1].split(',')[0]
                street_list.append(street)

                neighborhood = string_adress.split('>')[1].split(',')[1]
                neighborhood_list.append(neighborhood)

        # Contém quartos, banheiros e vagas abaixo:
        m_squared = soup.find_all('span', class_="whitespace-nowrap text-foxter-brand-900")
        for m in m_squared:
            if m_squared.index(m) == 0 or m_squared.index(m)%4 == 0:
                m_string = str(m)
                m_string = (m_string.split('>')[2])
                msquare = []
                for char in m_string:
                    if char.isdigit():
                        msquare.append(str(char))
                joined = float(''.join(msquare))/100
                m_squared_list.append(joined)

        code = soup.find_all('div', class_="text-xs text-slate-500 cursor-pointer") 
        for c in code:
            c_string = str(c) 
            if i == 1: 
                c_string = c_string.split('>')[2].split('<')[0]
                code_list.append(c_string)
            else:
                c_string = c_string.split('>')[1].split(' ')[1].split('<')[0]
                code_list.append(c_string)

    else:
        print("Error")
        # Print the response content as text
        #print(response.text)
df = pd.DataFrame()
df["Code"] = code_list
df["Neighborhood"] = neighborhood_list
df["Price"] = prices_list
df["m²"] = m_squared_list
df["Street"] = street_list
df["Price/m²"] = round((df["Price"]/df['m²']),3)

print(df['Price'])
df.to_csv('Data\\Webscrape_Data_Brute.csv')


df_media = pd.DataFrame()
df_media = df.groupby('Neighborhood')['Price/m²'].mean()
df_media = df_media.to_frame()
df_media = df_media.sort_values(by="Price/m²",ascending=False)
df_media.to_csv('Data\\Webscrape_Data_Avg.csv')

print(df.dtypes)

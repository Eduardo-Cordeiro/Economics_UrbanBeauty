import requests
from bs4 import BeautifulSoup

pages = int(10)


##interando por todas as paginas do site
for i in range(pages):
    ##Obtendo o HTML
   
    url = 'https://www.foxterciaimobiliaria.com.br/imoveis/a-venda/em-porto-alegre-rs?page='+str(i)

# Send a GET request to the URL
    response = requests.get(url)
# Check if the request was successful
    if response.status_code == 200:
        print('Success!')
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        prices = soup.find_all('h1', class_="font-bold text-xl text-foxter-brand-700")
        adress = soup.find_all('div', class_="flex text-sm justify-start text-foxter-brand-900")
        # Contém quartos, banheiros e vagas abaixo:
        m_squared = soup.find_all('span', class_="whitespace-nowrap text-foxter-brand-900")
        code = soup.find_all('div', class_="text-xs text-slate-500 cursor-pointer")
        for i in code:
            print(i)   
    else:
        print("Error")
        # Print the response content as text
        #print(response.text)

import requests
from bs4 import BeautifulSoup
from lxml import etree

def todosProductos(producto):

    lista_titulos = []
    lista_url = []
    lista_precio = []
    siguiente = 'https://listado.mercadolibre.com.ar/'+ producto

    while True:

        r = requests.get(siguiente)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content,'html.parser')
            #Titulo
            titulo = soup.find_all('h2',attrs={"class":"ui-search-item__title shops__item-title"})
            titulos = [i.text for i in titulo]
            lista_titulos.extend(titulos)
            #Url
            urls = soup.find_all('a',attrs={"class":"ui-search-item__group__element shops__items-group-details ui-search-link"})
            urls = [i.get('href') for i in urls]
            lista_url.extend(urls)
            #Precio
            dom = etree.HTML(str(soup))
            precios = dom.xpath('//li[@class="ui-search-layout__item shops__layout-item"]//div[@class="ui-search-result__content-columns shops__content-columns"]/div[1]/div[1]//div[@class="ui-search-price__second-line shops__price-second-line"]//span[@class="andes-money-amount__fraction"]')
            precios = [i.text for i in precios]
            lista_precio.extend(precios)

            ini = soup.find('span', attrs={"class":"andes-pagination__link"}).text
            ini = int(ini)

            can = soup.find('li', attrs={"class":"andes-pagination__page-count"})
            can = can.text.split(" ")[1]
            can = int(can)

        else:
            break

        print(ini, can)

        if ini == can:
            break

        #siguiente = dom.xpath('//div[@class="ui-search-pagination shops__pagination-content"]/ul//li[contains(@class,"--next")]/a')[0].get('href')
        siguiente = dom.xpath('//div[@class="ui-search-pagination shops__pagination-content"]//li[contains(@class,"--next")]/a')[0].get('href')
    return lista_titulos, lista_url, lista_precio

def limite_producto(producto, limite):

    lista_titulos = []
    lista_url = []
    lista_precio = []
    siguiente = 'https://listado.mercadolibre.com.ar/'+ producto

    while True:

        r = requests.get(siguiente)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content,'html.parser')
            #Titulo
            titulo = soup.find_all('h2',attrs={"class":"ui-search-item__title shops__item-title"})
            titulos = [i.text for i in titulo]
            lista_titulos.extend(titulos)
            #Url
            urls = soup.find_all('a',attrs={"class":"ui-search-item__group__element shops__items-group-details ui-search-link"})
            urls = [i.get('href') for i in urls]
            lista_url.extend(urls)
            #Precio
            dom = etree.HTML(str(soup))
            precios = dom.xpath('//li[@class="ui-search-layout__item shops__layout-item"]//div[@class="ui-search-result__content-columns shops__content-columns"]/div[1]/div[1]//div[@class="ui-search-price__second-line shops__price-second-line"]//span[@class="andes-money-amount__fraction"]')
            precios = [i.text for i in precios]
            lista_precio.extend(precios)

            ini = soup.find('span', attrs={"class":"andes-pagination__link"}).text
            ini = int(ini)

            can = soup.find('li', attrs={"class":"andes-pagination__page-count"})
            can = can.text.split(" ")[1]
            can = int(can)

        else:
            break

        print(ini, can)
        if len(lista_titulos)>=int(limite):
            return lista_titulos[:limite], lista_url[:limite], lista_precio[:limite]

        if ini == can:
            break

        #siguiente = dom.xpath('//div[@class="ui-search-pagination shops__pagination-content"]/ul//li[contains(@class,"--next")]/a')[0].get('href')
        siguiente = dom.xpath('//div[@class="ui-search-pagination shops__pagination-content"]//li[contains(@class,"--next")]/a')[0].get('href')
    return lista_titulos, lista_url, lista_precio
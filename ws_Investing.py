#Bibliotecas
import pandas as pd
from bs4 import BeautifulSoup
import requests
import cfscrape

def Investing_WS():

    lista_noticias=[]
    url = "https://br.investing.com/news/most-popular-news"
    scraper = cfscrape.create_scraper()
    resposta = scraper.get(url)
    conteudo = resposta.content

    soup = BeautifulSoup(conteudo, "html.parser")
    card_mais_lidas = soup.find("div",{"class":"largeTitle"})
    noticias = card_mais_lidas.find_all("a",{"class":"title"})

    for noticia in noticias:
        titulo = noticia.text
        link = "https://br.investing.com"+noticia["href"]
        lista_noticias.append([titulo,link])
    dataframe = pd.DataFrame(lista_noticias,columns=["Título","Link"])
    return dataframe
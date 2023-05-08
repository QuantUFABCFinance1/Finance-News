#bibliotecas
import pandas as pd
from bs4 import BeautifulSoup
import requests

def ValorEconomico_WS():

    url = "https://valor.globo.com/financas/"
    headers = {'user-agent': 'Mozilla/5.0'}

    resposta = requests.get(url,headers=headers)
    conteudo = resposta.content

    soup = BeautifulSoup(conteudo, "html.parser")
    card_mais_lidas = soup.find("div",{"class":"card-container bastian-card-mobile theme-font-primary card-mais-lidas valor"})
    noticias = card_mais_lidas.find_all("a")
    
    lista_noticias=[]
    
    for noticia in noticias:
        titulo = noticia.text
        link = noticia["href"]
        if titulo != " Mais Lidas ":
            lista_noticias.append([titulo,link])
        dataframe = pd.DataFrame(lista_noticias,columns=["Título","Link"])
        
    return dataframe

ve = ValorEconomico_WS()
ve
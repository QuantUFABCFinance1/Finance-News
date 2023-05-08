    #Bibliotecas
import pandas as pd
import requests
from bs4 import BeautifulSoup

def BloomBerg_WS():


    #parametros para conexão

    url = 'https://www.bloomberglinea.com.br/mercados/'
    headers = {'user-agent' : 'Mozilla/5.0'}

    #Conexão com o site
    resposta = requests.get(url,headers=headers)
    conteudo = resposta.content

    #HTML
    soup = BeautifulSoup(conteudo, "html.parser")
    noticias = soup.findAll('div', attrs={'class': 'flex flex-col lg:flex-col h-full false'})

    #Lista para guardar o link e o titulo
    lista_noticias = []

    #looping para pegar todos os links e titulos da <a class>
    for noticia in noticias:

        Informação = noticia.find('a', attrs={'class': 'hover:text-hover hover:underline'})
        lista_noticias.append([Informação.text, 'https://www.bloomberglinea.com.br'+Informação['href']])
        #tem que adicionar 'https://www.bloomberglinea.com.br' na frente do link do href


    #Criar Dataframe com o título e link
    df = pd.DataFrame(lista_noticias, columns=["Titulo", "Link"])

    #Filtro de informações
    Chaves = ['Banco Central', 'Minério', 'Lucro', 'Fed',\
              'Copom', 'Selic', 'Inflação','Crise', 'Petróleo', 'Federal Reserve', 'Juros', 'Crédito', 'Commodities']

    df = df[df['Titulo'].str.contains("|".join(Chaves), na=False)]
    #Ultimas 5 noticias
    ultimas = df.head(5)
    return ultimas

bb = BloomBerg_WS()
bb
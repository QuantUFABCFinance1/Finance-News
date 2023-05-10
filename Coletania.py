#Importar Scrapp e bibliotecas
from ws_BloomBerg import BloomBerg_WS
from ws_ValorEconomico import ValorEconomico_WS
#from ws_investing import Investing_WS
import pandas as pd
from datetime import date

""" Juntar notícias para envio  """

    #Chamar Scrapping
bb = BloomBerg_WS()
ve = ValorEconomico_WS()
#in = Investing_WS()

coletania = pd.merge(bb, ve, 'outer')
#coletania = pd.merge(bb, ve, in, 'outer')
print('Noticias consolidadas.')

noticiasAletorias = coletania.sample(5)
print('Noticias escolhidas.')

""" Enviar noticias usadas para a base histórica """
import psycopg2 as pg
from conexoes import postgresql

#conexão com o postgreSQL

try:
    conn = postgresql()
except pg.Error as e:
    print(e)
    print('Conexão com o postgreSQL não foi realizada')
finally:
    cur = conn.cursor()
    print('Conexão com o postgreSQL realizada.')

#Carregar dados em lista para inseção
noticiasAletorias['DT_envio'] = date.today()
dadoslegado = noticiasAletorias.values.tolist()

try:
    print('Inicio da inserção.')
    query = "INSERT INTO legadonoticias (titulo, link, dt_envio) VALUES (%s, %s, %s)"
    cur.executemany(query, dadoslegado)
    conn.commit()
except pg.Error as e:
    print(e)
    pass
finally:
    cur.close()
    conn.close()
    print('Fim da execução.')
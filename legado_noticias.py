""" Enviar noticias usadas para a base histórica """
import psycopg2 as pg
from datetime import date
from conexoes import postgresql
from Coletania import coletania

#conexão com o postgreSQL

noticiasAleatorias = coletania()

try:
    conn = postgresql()
except pg.Error as e:
    print(e)
    print('Conexão com o postgreSQL não foi realizada')
finally:
    cur = conn.cursor()
    print('Conexão com o postgreSQL realizada.')

#Carregar dados em lista para inseção
noticiasAleatorias['DT_envio'] = date.today()
dadoslegado = noticiasAleatorias.values.tolist()

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
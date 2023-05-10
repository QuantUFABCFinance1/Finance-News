#Importar Scrapp e bibliotecas
from ws_BloomBerg import BloomBerg_WS
from ws_ValorEconomico import ValorEconomico_WS
#from ws_investing import Investing_WS
import pandas as pd

def coletania():
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
    return noticiasAletorias

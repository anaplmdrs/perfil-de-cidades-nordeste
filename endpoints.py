import requests
import json

def extrai_dados_api (url: str) -> list:
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f'Erro ao conectar ao endoint {url}: {error}')
        return []

##ENDPOINTS   
#[TOTAL DE POPULAÇÃO POR ZONA URBANA OU RURAL]
#10089- População residente, total e quilombola, por sexo e grupos de idade, segundo localização e situação do domicílio
#zona rural, fora do territorio quilombola, nordeste. População total.
endpoint1 = 'https://servicodados.ibge.gov.br/api/v3/agregados/10089/periodos/2022/variaveis/93?localidades=N6[N2[2]]&classificacao=2[6794]|58[95253]|2661[60028]|1[2]'
#zona urbana, fora de territorio quilombola, nordeste. população total
endpoint2 = 'https://servicodados.ibge.gov.br/api/v3/agregados/10089/periodos/2022/variaveis/93?localidades=N6[N2[2]]&classificacao=2[6794]|58[95253]|2661[60028]|1[1]'

#[TOTAL DE POPULAÇÃO COM ZONA DE ACESSO A INTERNET]
#9936- Domicílios particulares permanentes ocupados, por existência de conexão domiciliar à Internet, condição de ocupação do domicílio e tipo do domicílio
# #População total com acesso a internet em domicílio.
endpoint3 = 'https://servicodados.ibge.gov.br/api/v3/agregados/9936/periodos/2022/variaveis/381?localidades=N6[N2[2]]&classificacao=2072[77585]|63[95826]|125[2932]'
#Qtd. domicílios sem acesso a internet em domicílio.
endpoint4 = 'https://servicodados.ibge.gov.br/api/v3/agregados/9936/periodos/2022/variaveis/381?localidades=N6[N2[2]]&classificacao=2072[77586]|63[95826]|125[2932]'
#População não alfabetizada
endpoint5 ='https://servicodados.ibge.gov.br/api/v3/agregados/10092/periodos/2022/variaveis/950?localidades=N6[N2[2]]&classificacao=59[1023]|2[6794]|58[95253]|2661[32776,60028]|1[6795]'
#População com superior completo
endpoint6 ='https://servicodados.ibge.gov.br/api/v3/agregados/10064/periodos/-6/variaveis/1920?localidades=N2[2]|N6[N2[2]]&classificacao=2082[78032]|58[95253]'
# Domicílios particulares permanentes ocupados
endpoint7 = 'https://servicodados.ibge.gov.br/api/v3/agregados/10109/periodos/2022/variaveis/381?localidades=N6[N2[2]]&classificacao=67[10972]|2661[32776,60028]|1[6795]'
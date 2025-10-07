import warnings
warnings.filterwarnings('ignore')
from pprint import pprint
import requests 
import pandas as pd
import sys

#A função faz o tratamento de todos os endpoints da API 'agregados' do IBGE
def processar_dados_populacao_api(api_response_data: list) -> pd.DataFrame:
    
    if not isinstance(api_response_data, list) or not api_response_data:
        print("Erro: A entrada da API não é uma lista válida ou está vazia.")
        return pd.DataFrame() # Retorna um DataFrame vazio

    # Acessar o primeiro (e único) dicionário da lista de resposta
    data_entry = api_response_data[0]

    if 'classificacoes' not in data_entry or 'series' not in data_entry:
        print("Erro: A estrutura da API não contém as chaves 'classificacoes' ou 'series' esperadas.")
        return pd.DataFrame()

    # --- Extrair dados de 'classificacoes' uma única vez ---
    common_classificacoes = data_entry['classificacoes']

    localizacao_domicilio = None
    situacao_domicilio = None

    for classificacao_item in common_classificacoes:
        if classificacao_item['nome'] == 'Localização do domicílio':
            localizacao_domicilio = list(classificacao_item['categoria'].values())[0]
        elif classificacao_item['nome'] == 'Situação do domicílio':
            situacao_domicilio = list(classificacao_item['categoria'].values())[0]

    # --- Inicializar lista para armazenar os dados extraídos para cada cidade ---
    extracted_data = []

    # --- Iterar sobre a lista de 'series' para obter dados de cada cidade ---
    for serie_item in data_entry['series']:
        localidade_nome = serie_item['localidade']['nome']
        localidade_id = serie_item['localidade']['id']
        valor_2022 = serie_item['serie']['2022']

        # Adicionar os dados combinados para a cidade atual
        extracted_data.append({
            'localização_domicilio': localizacao_domicilio,
            'municipio': localidade_nome,
            'cod_ibge': localidade_id,
            'situacao_domicilio': situacao_domicilio,
            'qtd_populacao': valor_2022
        })

    # Criar um DataFrame a partir dos dados extraídos
    df = pd.DataFrame(extracted_data)
    return df
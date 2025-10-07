import warnings
warnings.filterwarnings('ignore')
from pprint import pprint
import requests 
import pandas as pd
import sys
import logging
from planilhas import df_planilhas
from endpoints import extrai_dados_api, endpoint1, endpoint2, endpoint3, endpoint4, endpoint5, endpoint6,endpoint7
from processando_dados import processar_dados_populacao_api

logging.basicConfig(
    filename='log-censo2022.log',             # nome do arquivo de log
    filemode='w',                         # sobrescreve o arquivo a cada execução (use 'a' para append)
    level=logging.INFO,                   # nível mínimo de log
    format='[%(levelname)s] %(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
def processar_multiplos_endpoints(*endpoints):
    dataframes_processados = []
    logging.info(f"Iniciando o processamento de {len(endpoints)} endpoints.")

    for i, endpoint in enumerate(endpoints, 1):
        logging.info(f"--- Processando Endpoint {i} ---")
        try:
            dados_brutos = extrai_dados_api(endpoint)
            if dados_brutos and 'resultados' in dados_brutos[0]:
                dados_tratados = dados_brutos[0]['resultados']
                df = processar_dados_populacao_api(dados_tratados)
                dataframes_processados.append(df)
                logging.info(f"Dados do Endpoint {i} processados com sucesso. DataFrame gerado com {len(df)} linhas.")
            else:
                logging.warning(f"Aviso: Não foi possível obter ou tratar os dados do Endpoint {i}. Retornando um DataFrame vazio.")
                dataframes_processados.append(pd.DataFrame())
        except Exception as e:
            logging.error(f"Erro inesperado ao processar o Endpoint {i}: {e}")
            dataframes_processados.append(pd.DataFrame())
            
    logging.info("Processamento de todos os endpoints concluído.")
    return tuple(dataframes_processados)

# Chama a função com todos os seus endpoints
df_cidade_a, df_cidade_b, df_internet_a, df_internet_b, df_alfabetizados, df_superior_completo, df_qtd_domicilios = processar_multiplos_endpoints(
    endpoint1, endpoint2, endpoint3, endpoint4, endpoint5, endpoint6,endpoint7
)

def renomear_coluna(df, coluna_antiga, coluna_nova):
    return df.rename(columns={coluna_antiga: coluna_nova})

def remover_colunas(df,colunas):
    return df.drop(columns=colunas, errors = 'ignore')

logging.info("Iniciando construção do dataframe censo 2022")
# Renomear colunas
logging.info('Renomeando colunas...')
df_cidade_a = renomear_coluna(df_cidade_a, 'qtd_populacao', 'qtd_pop_rural')
df_cidade_b = renomear_coluna(df_cidade_b, 'qtd_populacao', 'qtd_pop_urbana')
df_internet_a = renomear_coluna(df_internet_a, 'qtd_populacao', 'qtd_domicilios_conectados')
df_internet_b = renomear_coluna(df_internet_b, 'qtd_populacao', 'qtd_domicilios_desconectados')
df_alfabetizados = renomear_coluna(df_alfabetizados, 'qtd_populacao', 'qtd_pop_alfabetizada')
df_superior_completo = renomear_coluna(df_superior_completo, 'qtd_populacao', 'qtd_pop_sup_completo')
df_qtd_domicilios = renomear_coluna(df_qtd_domicilios, 'qtd_populacao', 'qtd_domicilios')
df_planilhas = df_planilhas.astype(str)
logging.info (f'Removendo colunas desnecessárias')
# Remover colunas desnecessárias
df_cidade_a = remover_colunas(df_cidade_a, ['situacao_domicilio'])
df_cidade_b = remover_colunas(df_cidade_b, ['situacao_domicilio'])
#tratamento para fazer merge do cod_ibge da api com o das planilhas
logging.info(f'Realizando merges')
df_censo = (
    df_cidade_a
    .merge(df_cidade_b[['cod_ibge', 'qtd_pop_urbana']], on='cod_ibge', how = 'left')
    .merge(df_internet_a[['cod_ibge', 'qtd_domicilios_conectados']], on='cod_ibge', how='left')
    .merge(df_internet_b[['cod_ibge', 'qtd_domicilios_desconectados']], on='cod_ibge', how='left')
    .merge(df_alfabetizados[['cod_ibge', 'qtd_pop_alfabetizada']], on='cod_ibge', how='left')
    .merge(df_superior_completo[['cod_ibge', 'qtd_pop_sup_completo']], on='cod_ibge', how='left')
    .merge(df_qtd_domicilios[['cod_ibge', 'qtd_domicilios']], on='cod_ibge', how='left')
)
df_censo2022 = remover_colunas(df_censo, ['localização_domicilio'])
df_censo2022['cod_ibge_tratado'] = df_censo['cod_ibge'].astype(str).str[:-1]
df_censo2022 = df_censo2022.merge(df_planilhas[[
            'cod_ibge_tratado', 
            'qtd_pop_pobre', 
            'qtd_pop_baixa_renda', 
            'qtd_pop_acima_sal_min', 
            'qtd_fam_cadunico'
        ]], 
        on='cod_ibge_tratado', 
        how='inner'
    )
logging.info(f'Construção do Censo 2022 concluída com sucesso')
df_censo2022.to_csv('df_censo2022.csv', index = False)
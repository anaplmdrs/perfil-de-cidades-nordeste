import warnings
warnings.filterwarnings('ignore')
import pandas as pd

familia_cad_unico = pd.read_csv('familias_cad_unico.csv')
pop_bolsa_familia = pd.read_csv('bolsa-familia-renda.csv')

familia_cad_unico = familia_cad_unico[familia_cad_unico['anomes_s'] == 202507]
pop_bolsa_familia = pop_bolsa_familia[pop_bolsa_familia['anomes_s'] == 202508]

pop_bolsa_familia = pop_bolsa_familia.rename(columns={
    'codigo_ibge': 'cod_ibge_tratado',
    'qtd_pes_pob': 'qtd_pop_pobre',
    'qtd_pes_baixa_renda': 'qtd_pop_baixa_renda',
    'qtd_pes_acima_meio_sm': 'qtd_pop_acima_meio_sal_min'
})
familia_cad_unico = familia_cad_unico.rename(columns={
    'codigo_ibge': 'cod_ibge_tratado',
    'cadun_qtd_familias_cadastradas_i': 'qtd_fam_cadunico'
})

df_planilhas = pop_bolsa_familia.merge(familia_cad_unico[['cod_ibge_tratado', 'qtd_fam_cadunico']], on='cod_ibge_tratado', how = 'left')
df_planilhas = df_planilhas.drop(columns = ['anomes_s'])
df_planilhas
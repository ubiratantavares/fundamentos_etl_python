import pandas as pd
import pandera as pa

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv('ocorrencia_2010_2020_modify.csv', delimiter=';', parse_dates=['ocorrencia_dia'], dayfirst=True)

# limpeza de dados do dataframe

## uma coluna especifica
#df.loc[df.ocorrencia_aerodromo == '****', ['ocorrencia_aerodromo']] = pd.NA # valores não informados

## em todas as colunas
df.replace(['**', '###!', '####', '****', '*****', 'NULL'], pd.NA, inplace=True)
print(df.head())

## contabilização das colunas com dados não informados
print(df.isna().sum())
print(df.isnull().sum())

## altera os valores <NA> na coluna total_recomendacoes com o valor 10.
#df.fillna(value={'total_recomendacoes': 10}, inplace=True)

# criar uma coluna
#df['total_recomendacoes_bkp'] = df.total_recomendacoes

# excluir uma coluna
#df.drop(['total_recomendacoes_bkp'], axis=1, inplace=True)

# excluir todas as linhas que contém os valores <NA>
# df.dropna()

# excluir as linhas das colunas informadas que contem <NA>
# df.dropna(subset=['ocorrencia_uf', 'ocorrencia_hora'], inplace=True)

# excluir linhas com valores duplicados
#df.drop_duplicates(inplace=True)






'''
# validação dos dados do dataframe
schema = pa.DataFrameSchema(columns={'codigo': pa.Column(pa.Int, required=False),
                                    'codigo_ocorrencia': pa.Column(pa.Int),
                                     'codigo_ocorrencia2': pa.Column(pa.Int),
                                     'ocorrencia_classificacao': pa.Column(pa.String),
                                     'ocorrencia_cidade': pa.Column(pa.String),
                                     'ocorrencia_uf': pa.Column(pa.String, pa.Check.str_length(2, 2)),
                                     'ocorrencia_aerodromo': pa.Column(pa.String),
                                     'ocorrencia_dia': pa.Column(pa.DateTime),
                                     'ocorrencia_hora': pa.Column(pa.String,
                                                                  pa.Check.str_matches(r'^([0-1]?[0-9]|[2][0-3]):([0-5][0-9])(:[0-5][0-9])?$'),
                                                                  nullable=True),
                                     'total_recomendacoes': pa.Column(pa.Int)})
print(schema.validate(df))
'''




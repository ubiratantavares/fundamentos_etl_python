import pandas as pd
import pandera as pa

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv('ocorrencia_2010_2020_modify.csv', delimiter=';', parse_dates=['ocorrencia_dia'], dayfirst=True)

# manipulação de dados no dataframe
print(df.loc[1, 'ocorrencia_cidade'])
print(df.loc[1:3])
print(df.loc[[10, 40]])
print(df.loc[:, 'ocorrencia_cidade'])

# verificação de existe uma coluna no dataframe com valores únicos
print(df.codigo_ocorrencia.is_unique)

df.set_index('codigo_ocorrencia', inplace=True)
print(df.head())

# limpeza de dados do dataframe
print(df.loc[40349, 'ocorrencia_cidade'])

df.reset_index(drop=True, inplace=True)
print(df.head())

df.loc[0, 'ocorrencia_aerodromo'] = 20

df.loc[df.ocorrencia_uf == 'SP', ['ocorrencia_classificacao']] = 'GRAVE'
'''
# tamanho do dataframe
print(df.shape)

# visualiza os 5 primeiros registros do dataframe
print(df.head())

# visualiza os 5 últimos registros do dataframe
print(df.tail())

# visualiza os tipos de dados do dataframe
print(df.dtypes)

# retorna o mês referente ao atributo ocorrencia_dia
# print(df.ocorrencia_dia.dt.month)


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



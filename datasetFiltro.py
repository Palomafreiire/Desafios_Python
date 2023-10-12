import pandas as pd 

#Usando a biblioteca pandas, faça alguns filtros  no dataset do link anterior

df_vacinas = pd.read_csv('vacinados_CERTO.csv')

#print(df_vacinas.info)

#Selecione as pessoas vacinadas de Recife do sexo feminino da cor parda e preta maior de 60 anos

#df_cor = df_vacinas.loc[df_vacinas['raca_cor'].isin(['PARDA', 'PRETA'])]
#df_idade = df_vacinas.loc[df_vacinas['idade'] > 60 ]

df_feminino = df_vacinas.loc[(df_vacinas['sexo'] == 'FEMININO') & (df_vacinas['idade'] > 60) & (df_vacinas['raca_cor'].isin(['PARDA', 'PRETA']))]

dados_filtros = df_feminino[['sexo', 'idade', 'raca_cor']]
print(dados_filtros)

#Selecione as pessoas  que se vacinaram nos meses de abril e maio do sexo masculino
df_masculino = df_vacinas.loc[(df_vacinas['sexo'] == 'MASCULINO')] 

# data = & (df_vacinas['data_vacinacao'].dt.month.isin([11, 12]))]


dados_filtros2 = df_masculino['sexo']
print(dados_filtros2)




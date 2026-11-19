import os
import pandas as pd
import sqlite3

# 1. Obter o diretório atual e carregar o CSV gerado na etapa anterior
diretorio_atual = os.getcwd()
caminho_csv = os.path.join(diretorio_atual, 'ipca_alimentacao_tratado.csv')

df = pd.read_csv(caminho_csv)

# 2. Conectar (ou criar) um banco de dados SQLite local chamado 'economia.db'
caminho_db = os.path.join(diretorio_atual, 'economia.db')
conn = sqlite3.connect(caminho_db)

# 3. Salvar o DataFrame como uma tabela SQL chamada 'tb_ipca'
df.to_sql('tb_ipca', conn, if_exists='replace', index=False)
print('Banco de dados relacional criado e dados importados com sucesso!\n')

# 4. Consultas SQL de Análise (Respondendo a perguntas de negócio)

# Pergunta 1: Quais foram os 5 meses com maior alta no IPCA Geral?
print('--- TOP 5 MAIORES ALTAS DO IPCA ---')
query_maiores_altas = """
    SELECT data, ipca_geral 
    FROM tb_ipca 
    ORDER BY ipca_geral DESC 
    LIMIT 5
"""
df_altas = pd.read_sql(query_maiores_altas, conn)
print(df_altas)
print('\n' + '=' * 50 + '\n')

# Pergunta 2: Qual a média geral da inflação no período analisado?
print('--- MÉDIA GERAL DA INFLAÇÃO DO PERÍODO (%) ---')
query_medias = """
    SELECT 
        AVG(ipca_geral) as media_ipca_geral
    FROM tb_ipca
"""
df_medias = pd.read_sql(query_medias, conn)
print(df_medias)

# Fechar a conexão com o banco de dados
conn.close()
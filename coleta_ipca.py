import os
import pandas as pd
import requests

# URL direta da Tabela 7060 do IPCA (Variação mensal)
url = "https://servicodados.ibge.gov.br/api/v3/agregados/7060/periodos/202301-202612/variaveis/63?localidades=N1[1]"

print("Baixando dados da API do IBGE...")
response = requests.get(url)

if response.status_code == 200:
  dados_json = response.json()
  print("Dados obtidos com sucesso!")
else:
  raise Exception(f"Erro ao acessar a API: {response.status_code}")

# Extração corrigida usando 'series' (no plural)
try:
  # O IBGE retorna 'series' com 's'
  serie_temporal = dados_json[0]["resultados"][0]["series"][0]["serie"]
  df_pivot = pd.DataFrame(
      list(serie_temporal.items()), columns=["ano_mes", "ipca_geral"]
  )
except Exception as e:
  print(f"Erro ao processar o JSON: {e}")
  raise

# Tratamento de dados
df_pivot["ipca_geral"] = pd.to_numeric(df_pivot["ipca_geral"], errors="coerce")
df_pivot["data"] = pd.to_datetime(df_pivot["ano_mes"], format="%Y%m")
df_pivot = df_pivot.sort_values("data").reset_index(drop=True)
df_pivot.fillna(0, inplace=True)

# Exportação para CSV
diretorio_atual = os.getcwd()
arquivo_saida = os.path.join(diretorio_atual, "ipca_alimentacao_tratado.csv")

df_pivot.to_csv(arquivo_saida, index=False, encoding="utf-8-sig")

print("\nArquivo criado com sucesso!")
print(f"Caminho completo: {arquivo_saida}")
print("\nPrimeiras 5 linhas dos dados:")
print(df_pivot.head(5))
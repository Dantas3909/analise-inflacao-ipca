# 📊 Análise de Inflação (IPCA) - End-to-End Data Analyst Project

Projeto de portfólio desenvolvido para demonstrar habilidades em engenharia e análise de dados, cobrindo todo o pipeline: desde a extração automatizada via API até o armazenamento em banco relacional e criação de dashboards gerenciais.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Python**: Extração de dados da API do IBGE (SIDRA), tratamento e limpeza de dados (`Pandas`, `Requests`, `OS`).
* **SQLite / SQL**: Criação de banco de dados relacional local (`economia.db`) e consultas analíticas de negócio.
* **Power BI**: Construção de painéis interativos para visualização de tendências e KPIs de inflação.

---

## ⚙️ Arquitetura do Projeto / Pipeline de Dados

1. **Extração (ETL):** O script Python consome os dados oficiais da Tabela 7060 do IPCA (SIDRA/IBGE), tratando os campos temporais e exportando uma base limpa.
2. **Armazenamento:** Os dados tratados são carregados automaticamente para um banco de dados relacional SQLite (`economia.db`) via Python.
3. **Análise SQL:** Consultas estruturadas respondem a perguntas de negócio (como os períodos de maiores picos inflacionários e médias do período).
4. **Visualização (Dashboard):** Conexão com o Power BI para exibir a evolução histórica da inflação através de gráficos de linha, colunas e cartões de KPI.

---

## 🚀 Como Executar o Projeto

1. Clone este repositório na sua máquina:
   ```bash
git clone [https://github.com/Dantas3909/analise-inflacao-ipca.git](https://github.com/Dantas3909/analise-inflacao-ipca.git)
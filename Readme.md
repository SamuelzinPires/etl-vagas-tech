# Pipeline ETL: Extração e Análise de Vagas Tech (Gupy)

Este projeto consiste na construção de um **Pipeline de Dados ETL (Extract, Transform, Load)** completo e automatizado, desenvolvido em Python. O objetivo principal é extrair centenas de vagas da área de tecnologia da plataforma Gupy, tratar os dados para extrair inteligência de negócio e armazená-los num banco de dados relacional.

##  Arquitetura do Projeto (Medallion Architecture)

O projeto foi estruturado seguindo as melhores práticas da Engenharia de Dados, dividindo o processo em etapas claras (Camadas Bronze, Prata e Ouro/Análise):

1. **Extract (`extrator.py`) - Camada Bronze:**
   - Realiza requisições HTTP na API oculta da Gupy.
   - Utiliza lógica de **Paginação (offset e limit)** para contornar limites da API e extrair dados em massa (centenas de vagas de uma só vez).
   - Salva os dados brutos de forma segura no formato `.csv` (`data/raw/`).

2. **Transform (`transformador.py`) - Camada Prata:**
   - Utiliza a biblioteca **Pandas** para atuar como uma "lavandaria de dados".
   - Padroniza campos e traduz os modelos de trabalho (on-site, remote, hybrid).
   - **Regra de Negócio Avançada:** Aplica expressões e o método `.apply()` para varrer os títulos das vagas e deduzir a **Senioridade** exigida (Júnior, Pleno, Sênior).
   - Salva os dados limpos num novo arquivo (`data/processed/`).

3. **Load (`carregador.py`):**
   - Transforma os dados limpos em tabelas relacionais.
   - Carrega automaticamente o DataFrame do Pandas para um **Banco de Dados SQLite** (`banco_de_vagas.db`), simulando o ambiente de um Data Warehouse real.

4. **Análise de Dados (`analise.py`):**
   - Script focado em responder a perguntas de negócio (*Business Intelligence*).
   - Conta a distribuição de vagas por nível de senioridade e ranqueia as empresas com mais vagas abertas.

## Tecnologias Utilizadas

* **Python 3**
* **Pandas** (Limpeza, Transformação e Análise de Dados)
* **Requests** (Comunicação com a API)
* **SQLite3** (Banco de Dados Relacional)
* **Git & GitHub** (Versionamento de Código)

## 📁 Estrutura de Diretórios

```text
projeto-etl-vagas-tech/
│
├── data/
│   ├── raw/             # Dados brutos originais (Camada Bronze)
│   └── processed/       # Dados limpos e Banco de Dados (Camada Prata)
│
├── src/
│   ├── extrator.py      # Script de Extração (API)
│   ├── transformador.py # Script de Limpeza (Pandas)
│   ├── carregador.py    # Script de Carga (SQLite)
│   └── analise.py       # Script de Análise Exploratória
│
├── .gitignore           # Oculta arquivos desnecessários/pesados do Git
└── README.md            # Documentação do projeto

Execute os scripts na ordem do Pipeline ETL:

Bash
python extrator.py       # Passo 1: Extrair
python transformador.py  # Passo 2: Limpar e Transformar
python carregador.py     # Passo 3: Salvar no Banco de Dados
python analise.py        # Passo 4: Ver os Insights do mercado
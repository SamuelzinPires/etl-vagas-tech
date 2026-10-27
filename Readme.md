# ETL Vagas Tech: vagas da área de dados na Gupy

Pipeline **ETL (Extract, Transform, Load)** em Python que coleta vagas da área de **dados** na plataforma Gupy, trata os campos com Pandas, carrega o resultado num banco **SQLite** e responde a duas perguntas: quantas vagas existem por nível de senioridade e quais empresas têm mais vagas abertas.

Na execução registrada (março/2026), a extração trouxe **643 vagas**.

## Como o pipeline funciona

```text
API JSON da Gupy (busca "dados", 10 vagas por requisição)
        │  extrator.py: paginação por offset até a API devolver uma página vazia
        ▼
data/raw/vagas_gupy.csv            (dado bruto)
        │  transformador.py: traduz o formato de trabalho e deduz a senioridade
        ▼
data/processed/vagas_limpas.csv    (dado tratado)
        │  carregador.py: DataFrame → tabela "vagas"
        ▼
data/processed/banco_de_vagas.db   (SQLite)
```

O `analise.py` lê o CSV tratado e imprime o resumo no terminal.

## Etapas

1. **Extract (`extrator.py`)**
   - Consome o endpoint de busca do portal de vagas da Gupy (`employability-portal.gupy.io/api/v1/jobs?jobName=dados`), que devolve JSON.
   - **Paginação por `offset` e `limit`:** pede 10 vagas por vez e avança o offset até a API devolver uma lista vazia. Se a resposta não for `200`, o loop para e mostra o status.
   - Usa `.get()` com valor padrão em cada campo, para uma vaga incompleta não derrubar a extração.
   - Guarda título, empresa, formato de trabalho e link em `data/raw/vagas_gupy.csv`.

2. **Transform (`transformador.py`)**
   - Traduz o formato de trabalho: `on-site`, `remote` e `hybrid` viram Presencial, Remoto e Híbrido.
   - Deduz a **senioridade** pelo título da vaga com `.apply()` e palavras-chave (Júnior, Pleno, Sênior ou Não Informado).
   - Salva em `data/processed/vagas_limpas.csv`.

3. **Load (`carregador.py`)**
   - Carrega o CSV tratado na tabela `vagas` de um banco SQLite (`data/processed/banco_de_vagas.db`) com `df.to_sql`.
   - Usa `if_exists='replace'`: cada execução substitui a tabela inteira, então rodar de novo não duplica as linhas no banco.

4. **Análise (`analise.py`)**
   - Mostra a distribuição de vagas por senioridade e as 5 empresas com mais vagas abertas.

## Tecnologias

* **Python 3**
* **Requests** (chamadas à API)
* **Pandas** (limpeza, transformação e análise)
* **SQLite3** (banco relacional local)

## Estrutura de diretórios

```text
projeto-etl-vagas-tech/
│
├── data/                # fora do Git (.gitignore)
│   ├── raw/             # dado bruto da API
│   └── processed/       # CSV tratado e banco SQLite
│
├── src/
│   ├── extrator.py      # extração (API + paginação)
│   ├── transformador.py # limpeza e transformação (Pandas)
│   ├── carregador.py    # carga no SQLite
│   └── analise.py       # resumo das vagas
│
├── .gitignore
└── Readme.md
```

## Como rodar

```bash
git clone https://github.com/SamuelzinPires/etl-vagas-tech.git
cd etl-vagas-tech

python -m venv venv
.\venv\Scripts\Activate.ps1      # Windows PowerShell
pip install requests pandas

mkdir data/raw, data/processed   # as pastas de dados ficam fora do Git
```

Os scripts usam caminhos relativos (`../data/...`), por isso rodam de dentro da pasta `src/`, nesta ordem:

```bash
cd src
python extrator.py       # 1. extrai as vagas da API
python transformador.py  # 2. trata os dados
python carregador.py     # 3. carrega no SQLite
python analise.py        # 4. mostra o resumo
```

## Histórico

A primeira versão (24/02/2026) raspava o HTML da página com **BeautifulSoup**. Em 27/02 o extrator passou a consumir a **API JSON** do portal: o dado já vem estruturado, a extração não depende do layout do site e a paginação fica simples (offset + limit). O BeautifulSoup não faz mais parte do código.

## Limitações conhecidas

- **Senioridade por trecho de palavra:** a regra procura `jr`, `pl` e `sr` em qualquer parte do título. Com isso, palavras como "Plataforma" e "Aplicações" fazem a vaga cair como Pleno, inclusive quando o título também diz Sênior (o teste de Pleno vem antes). A correção seria procurar palavras inteiras, com regex e `\b`.
- **Sem deduplicação:** se a mesma vaga aparecer em duas páginas (a lista pode mudar durante a extração), ela entra duas vezes.
- **Sem histórico:** cada execução substitui o resultado anterior, então não dá para comparar o mercado entre datas.

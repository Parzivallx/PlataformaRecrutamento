---

# 📄 Explicação do Arquivo `recrutamento.py`

Este script implementa uma plataforma interativa de linha de comando para **recrutamento e seleção de candidatos**. Suas principais características são a geração de uma base de dados simulada e um sistema de **filtros em cascata** para busca e ordenação de perfis.

---

## 📦 Estrutura de Dados e Geração

### 🏭 Fábrica de Candidatos
Para simular um ambiente realista, o script gera uma grande base de dados de forma procedural.
- **`NOMES...`, `SOBRENOMES...`, `LOCALIZACOES...`**: Listas que servem como base para a criação de nomes e localizações aleatórias.
- **`SKILLS_POR_FORMACAO`**: Dicionário que associa áreas de formação a um conjunto de habilidades técnicas coerentes, garantindo a criação de perfis realistas.
- **`criar_candidatos(...)`**:
  ```python
  def criar_candidatos(formacao: str, quantidade: int) -> List['Candidato']:
  ```
  Função que gera uma lista de objetos `Candidato` com atributos aleatórios (experiência, habilidades, etc.) baseados na formação especificada.

### ✅ Classe `Candidato`
Define a estrutura de dados para cada candidato.
```python
class Candidato:
    def __init__(...)
```
**Atributos:**
- `nome`: Nome completo do candidato.
- `habilidades`: Lista de habilidades técnicas (ex: `["python", "sql"]`).
- `formacao`: Curso superior do candidato.
- `localizacao`: Estado ou cidade (ex: `"SP"`).
- `experiencia`: Tempo de experiência em anos.
- `data_candidatura`: Data da candidatura no formato `YYYY-MM-DD`.
- `resumo`: Texto descritivo com perfil profissional.

**Métodos:**
- `match_relevancia`: Conta quantas habilidades do candidato coincidem com os requisitos da vaga.
- `score_adequacao`: Calcula um score de compatibilidade, com peso em habilidades e experiência.
- `__repr__`: Define a representação textual curta do objeto.
- `__str__`: Define a representação textual longa e detalhada do objeto.

---

## ⚙️ Funções e Lógica Principal

### 🧠 Funções de Apoio (Helpers)
- **`normalizar_string(texto)`**: Remove acentos e converte o texto para minúsculas. Essencial para buscas flexíveis e insensíveis a maiúsculas/minúsculas e acentuação.
- **`MAPA_DE_TERMOS`**: Um dicionário que mapeia abreviações e sinônimos a termos de busca (ex: `cc` -> `ciencia da computacao`). Utilizado para buscas "inteligentes".
- **`selecionar_opcao(...)`**: Função de interface que exibe uma lista de opções numerada e processa a entrada do usuário, que pode ser tanto o texto quanto o número da opção.

### 📊 Função `ordenar_candidatos`
```python
def ordenar_candidatos(lista_de_candidatos, criterios, requisitos=None):
```
Ordena a lista de candidatos filtrados com base em uma lista de critérios.
- `"experiencia"`: Mais experientes primeiro.
- `"data"`: Candidaturas mais recentes primeiro.
- `"score"`: Pelo `score_adequacao` calculado.
- `"relevancia"`: Pelo número de habilidades compatíveis.

### 🚀 Função `filtro_em_cascata`
Esta é a função principal que controla o fluxo interativo do programa.
```python
def filtro_em_cascata():
```
**Principais Funcionalidades:**
- **Lógica em Cascata**: A cada filtro aplicado pelo usuário (ex: por Formação), as opções para o filtro seguinte (ex: Habilidades) são recalculadas com base nos candidatos restantes.
- **Menus Dinâmicos**: As listas de opções para Formação e Habilidades são geradas dinamicamente e exibem a contagem de candidatos em cada item, além de abreviações.
- **Busca Flexível**: A busca por texto utiliza a função `normalizar_string` e o `MAPA_DE_TERMOS`, permitindo buscas parciais, por abreviações e sem sensibilidade a acentos.
- **Sistema de Sugestão**: Se uma habilidade não é encontrada no grupo atual de candidatos, o sistema informa e sugere outras formações onde a habilidade está presente.
- **Pré-visualização**: Antes da ordenação, exibe uma tabela resumida dos candidatos encontrados com seus respectivos scores, relevância e outros dados, para auxiliar na escolha do critério de ordenação.

---

## ⚡ Execução

O script é uma aplicação de linha de comando. Para rodar, utilize:
```bash
python recrutamento.py
```

---

## 🎯 Objetivo

Este script serve como um protótipo robusto de um sistema de triagem de candidatos. Ele pode ser a base para:
- Desenvolvimento de uma aplicação web completa.
- Ferramentas de automação para departamentos de RH.
- Um projeto de portfólio para demonstrar habilidades em Python, design de software e lógica de programação.

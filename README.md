```
PlataformaRecrutamento/
│
├── README.md
├── recrutamento.py
├── .gitignore
└── LICENSE
```
-----

# 🚀 Plataforma de Recursos Humanos e Recrutamento

Este projeto é uma simulação de uma plataforma interativa de recrutamento via linha de comando (CLI), integrando funcionalidades avançadas de **busca em cascata** e **ordenação inteligente** para facilitar a triagem de candidatos. É uma ferramenta para agilizar e otimizar processos seletivos.

-----

## ✨ Funcionalidades

### 🔍 Busca Inteligente

Os recrutadores podem encontrar os candidatos ideais através de um **filtro interativo em cascata**, onde cada escolha refina as opções para o passo seguinte.

  - **Busca Flexível**: A seleção de filtros aceita nome completo, parte da palavra, abreviação ou o número da opção no menu.
  - **Menus Dinâmicos**: As opções de **Formação** e **Habilidades** exibem a contagem de candidatos disponíveis em cada categoria, ajudando na tomada de decisão.
  - **Geração de Dados**: O script possui uma "fábrica de talentos" que gera uma base de dados rica e realista com mais de 50 candidatos para uma simulação completa.
  - **Sistema de Sugestão**: Caso uma habilidade não seja encontrada em um grupo filtrado, o sistema informa e sugere outras formações que possuem tal competência.

### 📊 Ordenação Informada

Após a filtragem, os candidatos encontrados são apresentados de forma estratégica.

  - **Pré-visualização de Dados**: Uma lista resumida é exibida com os dados-chave de cada candidato (Score, Relevância, Experiência) *antes* da ordenação final.
  - **Ordenação por Múltiplos Critérios**: O usuário pode então ordenar a lista final com base em:
      - **Relevância**: Quantidade de habilidades que correspondem aos requisitos.
      - **Anos de experiência**.
      - **Data da candidatura**.
      - **Pontuação de adequação (Score)**: Uma combinação de relevância e experiência.

-----

## 🤝 Sinergia entre Busca e Ordenação

Diferente de um script simples, a sinergia aqui é total e interativa. O usuário é guiado por um funil de seleção onde a **busca** e a **ordenação** são etapas de um mesmo fluxo de trabalho contínuo, garantindo que o recrutador sempre tenha o máximo de informação para focar nos perfis mais promissores.

-----

## ⚙️ Como usar?

1.  **Pré-requisitos**: Certifique-se de ter o **Python 3.7 ou superior** instalado.
2.  **Execução**: Salve o código como `recrutamento.py` e execute o seguinte comando no seu terminal, na pasta onde o arquivo está salvo:
    ```bash
    python recrutamento.py
    ```
3.  **Interação**: Siga as instruções dos menus interativos para filtrar, visualizar e ordenar os candidatos.

-----

## 💻 Exemplo Rápido de Interação

```bash
$ python recrutamento.py

--- Nova Busca ---
=> Opções de Formação:
   1 - Engenharia de Software (es) [6 candidatos]
   ...
Digite o nome, parte do nome, abreviação ou número: eng

=> Habilidades disponíveis no grupo:
   1 - automação industrial [5 candidatos]
   ...
Digite o nome, parte do nome, abreviação ou número: python

--- Candidatos Encontrados (Pré-visualização) ---
1. Ana Souza         | Relevância: 1  | Score: 13  | Exp: 3a | Data: 2024-06-01
...

Como deseja ordenar os resultados? (pode escolher vários, ex: 1, 4)
   1 - relevancia
   2 - score
   ...
=> Critérios (padrão: score, experiencia): 2
```

-----

## 👥 Colaboradores

Este projeto foi desenvolvido e mantido por alunos do curso de Engenharia de Software do Centro Universitário do Distrito Federal (UDF), com conhecimentos desenvolvidos na disciplina de Estrutura de Dados.

```
|Letícia Castro de Souza  
|Emmanuel Ferreira Gomes  
|Lucas Eduardo Barreto de Oliveira  
|João Pedro Reis Rios  
|Júlio Brenno Lopes Tavares
```

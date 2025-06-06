```
PlataformaRecrutamento/
│
├── README.md
├── recrutamento.py
├── .gitignore
└── LICENSE
```


# 🚀 Plataforma de Recursos Humanos e Recrutamento

Este projeto simula uma plataforma simples de recrutamento, integrando funcionalidades de **busca** e **ordenação** para facilitar a triagem de candidatos com base em critérios diversos. É uma ferramenta para agilizar e otimizar processos seletivos.

## ✨ Funcionalidades

### 🔍 Busca
Recrutadores podem buscar candidatos na base de dados aplicando filtros como:  
- **Habilidades** (ex: Python, Java, SQL).
- **Experiência profissional** mínima em anos.
- **Formação acadêmica** (ex: Engenharia, Ciência da Computação).
- **Localização geográfica** (ex: SP, RJ).
- **Palavras-chave no currículo** ou resumo profissional.

### 📊 Ordenação
Após a busca, os candidatos encontrados podem ser ordenados por:  
- **Relevância**: quantidade de habilidades que batem com os requisitos da vaga.
- **Anos de experiência**.
- **Data da candidatura** (mais recente ou mais antiga).
- **Score de adequação**: uma combinação do match de habilidades com a experiência, configurável para definir candidatos mais alinhados.

### 🤝 Sinergia entre Busca e Ordenação 
A busca retorna um pool de candidatos que atendem aos critérios básicos, e a ordenação classifica esse grupo para que o recrutador foque primeiro nos perfis mais promissores, tornando o processo de seleção mais eficiente.

## ⚙️ Como usar?

1. **Configurar candidatos:** no arquivo `recrutamento.py` há uma lista simulada de candidatos para teste.  
2. **Definir filtros:** no script principal, especifique os requisitos da vaga (habilidades, localização, etc).  
3. **Buscar candidatos:** chama-se a função `buscar_candidatos` passando os filtros desejados.  
4. **Ordenar candidatos:** usa-se `ordenar_candidatos` para ordenar os resultados pelo critério que preferir.  
5. **Visualizar resultados:** imprimir ou manipular a lista final de candidatos ordenados.

## 💻 Exemplo rápido

```python
requisitos_vaga = ["Python", "SQL"]
filtrados = buscar_candidatos(candidatos, requisitos=requisitos_vaga, localizacao="SP")
ordenados = ordenar_candidatos(filtrados, criterio="score", requisitos=requisitos_vaga)

for c in ordenados:
    print(c)

```

## 👥 Colaboradores
Este projeto foi desenvolvido e mantido pelos alunos do curso de Engenharia de Software do Centro Universitário do Distrito Federal (UDF), com conhecimentos
desenvolvidos na disciplina de Estrutura de Dados.

```
|Letícia Castro de Souza  
|Emmanuel Ferreira Gomes  
|Lucas Eduardo Barreto de Oliveira  
|João Pedro Reis Rios  
|Júlio Brenno Lopes Tavares
```


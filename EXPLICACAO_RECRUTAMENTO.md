
# 📄 Explicação do Arquivo `recrutamento.py`

Este script simula uma plataforma simples de **recrutamento e seleção de candidatos**, com foco em busca 🔍 e ordenação 📊 de perfis com base em critérios comuns no mercado de RH.

---

## 📦 Estrutura Principal

### ✅ Classe `Candidato`

Define os atributos e comportamentos de um candidato:

```python
class Candidato:
    def __init__(...)
```

**Atributos:**
- `nome`: Nome completo do candidato
- `habilidades`: Lista de habilidades técnicas (ex: `["Python", "SQL"]`)
- `formacao`: Curso superior do candidato
- `localizacao`: Estado ou cidade (ex: `"SP"`)
- `experiencia`: Tempo de experiência em anos
- `data_candidatura`: Data da candidatura no formato `YYYY-MM-DD`
- `resumo`: Texto descritivo com perfil profissional

**Métodos:**
- `match_relevancia`: Conta quantas habilidades do candidato coincidem com os requisitos da vaga
- `score_adequacao`: Calcula um score de compatibilidade, com peso em habilidades e experiência
- `__repr__`: Representação em texto ao imprimir o candidato

---

## 🔍 Função `buscar_candidatos`

```python
def buscar_candidatos(candidatos: List[Candidato], ...)
```

Filtra os candidatos com base nos critérios:
- `requisitos` (habilidades)
- `formacao`
- `localizacao`
- `experiencia_min`
- `palavra_chave` (no resumo)

**Exemplo:**

```python
filtrados = buscar_candidatos(candidatos, requisitos=["Python"], localizacao="SP")
```

---

## 📊 Função `ordenar_candidatos`

```python
def ordenar_candidatos(candidatos: List[Candidato], criterio="relevancia", ...)
```

Ordena a lista de candidatos com base em:
- `"experiencia"`: mais experientes primeiro
- `"data"`: por ordem de candidatura
- `"score"`: usando a fórmula `relevância * 10 + experiência`
- `"relevancia"`: habilidades que batem com a vaga

**Exemplo:**

```python
ordenados = ordenar_candidatos(filtrados, criterio="score", requisitos=["Python"])
```

---

## 🧪 Exemplo de uso

No final do script, o `if __name__ == "__main__"` executa um teste prático:

```python
# Filtra candidatos para SP com "Python" e "SQL"
filtrados = buscar_candidatos(...)

# Ordena os candidatos filtrados por score
ordenados = ordenar_candidatos(...)
```

---

## 🧠 Objetivo

Este script pode ser o ponto de partida para:
- Sistemas de triagem de currículos
- Ferramentas de recrutamento automatizadas
- Treinamento de modelos de IA com perfis fictícios

---

✍️ Criado como exemplo de projeto para estudos acadêmicos e técnicos.

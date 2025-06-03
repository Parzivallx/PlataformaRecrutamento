from datetime import datetime
from typing import List

class Candidato:
    def __init__(self, nome, habilidades, formacao, localizacao, experiencia, data_candidatura, resumo):
        self.nome = nome
        self.habilidades = habilidades  # lista de habilidades
        self.formacao = formacao
        self.localizacao = localizacao
        self.experiencia = experiencia  # em anos
        self.data_candidatura = datetime.strptime(data_candidatura, "%Y-%m-%d")
        self.resumo = resumo

    def match_relevancia(self, requisitos):
        return len([h for h in requisitos if h in self.habilidades])

    def score_adequacao(self, requisitos):
        return self.match_relevancia(requisitos) * 10 + self.experiencia

    def __repr__(self):
        return f"{self.nome} | {self.localizacao} | {self.experiencia} anos | {self.data_candidatura.date()}"


# Lista de candidatos simulada
candidatos = [
    Candidato("Ana Souza", ["Python", "SQL", "Git"], "Engenharia de Software", "SP", 3, "2025-06-01", "Trabalhou com análise de dados."),
    Candidato("Carlos Lima", ["Java", "Spring", "AWS"], "Ciência da Computação", "RJ", 5, "2025-05-30", "Backend e Cloud."),
    Candidato("Beatriz Rocha", ["Python", "Django", "HTML"], "Sistemas de Informação", "MG", 2, "2025-06-02", "Desenvolvedora web."),
    Candidato("Eduardo Nunes", ["C#", ".NET", "SQL Server"], "Engenharia da Computação", "SP", 4, "2025-06-01", "Experiência em sistemas corporativos."),
    Candidato("Fernanda Dias", ["Python", "Pandas", "Machine Learning"], "Estatística", "RS", 6, "2025-05-29", "Data scientist com foco em IA."),
]


# Função de busca com filtros
def buscar_candidatos(candidatos: List[Candidato], requisitos: List[str] = [],
                       formacao: str = None, localizacao: str = None,
                       experiencia_min: int = 0, palavra_chave: str = None):
    resultado = []
    for c in candidatos:
        if requisitos and not any(r in c.habilidades for r in requisitos):
            continue
        if formacao and formacao.lower() not in c.formacao.lower():
            continue
        if localizacao and localizacao.lower() != c.localizacao.lower():
            continue
        if c.experiencia < experiencia_min:
            continue
        if palavra_chave and palavra_chave.lower() not in c.resumo.lower():
            continue
        resultado.append(c)
    return resultado


# Função de ordenação
def ordenar_candidatos(candidatos: List[Candidato], criterio: str = "relevancia", requisitos: List[str] = []):
    if criterio == "experiencia":
        return sorted(candidatos, key=lambda c: c.experiencia, reverse=True)
    elif criterio == "data":
        return sorted(candidatos, key=lambda c: c.data_candidatura)
    elif criterio == "score":
        return sorted(candidatos, key=lambda c: c.score_adequacao(requisitos), reverse=True)
    else:  # relevancia (padrão)
        return sorted(candidatos, key=lambda c: c.match_relevancia(requisitos), reverse=True)


# Exemplo de uso
if __name__ == "__main__":
    requisitos_vaga = ["Python", "SQL"]
    print("--- Candidatos encontrados ---")
    filtrados = buscar_candidatos(candidatos, requisitos=requisitos_vaga, localizacao="SP")
    for c in filtrados:
        print(c)

    print("\n--- Ordenados por score de adequação ---")
    ordenados = ordenar_candidatos(filtrados, criterio="score", requisitos=requisitos_vaga)
    for c in ordenados:
        print(c)

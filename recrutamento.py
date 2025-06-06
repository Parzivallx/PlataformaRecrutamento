from datetime import datetime
from typing import List, Optional

class Candidato:
    def __init__(self, nome, habilidades, formacao, localizacao, experiencia, data_candidatura, resumo):
        self.nome = nome
        self.habilidades = [h.lower() for h in habilidades]  # normaliza
        self.formacao = formacao
        self.localizacao = localizacao
        self.experiencia = experiencia  # em anos
        try:
            self.data_candidatura = datetime.strptime(data_candidatura, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Data inválida para {nome}. Use o formato YYYY-MM-DD.")
        self.resumo = resumo

    def match_relevancia(self, requisitos: List[str]) -> int:
        return len([h for h in requisitos if h.lower() in self.habilidades])

    def score_adequacao(self, requisitos: List[str]) -> int:
        return self.match_relevancia(requisitos) * 10 + self.experiencia

    def __repr__(self):
        return f"{self.nome} | {self.localizacao} | {self.experiencia} anos | {self.data_candidatura.date()}"

    def __str__(self):
        return (
            f"{self.nome}, {self.formacao} ({self.localizacao}) - {self.experiencia} anos de experiência.\n"
            f"Data da candidatura: {self.data_candidatura.date()}\nResumo: {self.resumo}\n"
        )


# Lista de candidatos simulada
candidatos = [
    Candidato("Ana Souza", ["Python", "SQL", "Git"], "Engenharia de Software", "SP", 3, "2025-06-01", "Trabalhou com análise de dados."),
    Candidato("Carlos Lima", ["Java", "Spring", "AWS"], "Ciência da Computação", "RJ", 5, "2025-05-30", "Backend e Cloud."),
    Candidato("Beatriz Rocha", ["Python", "Django", "HTML"], "Sistemas de Informação", "MG", 2, "2025-06-02", "Desenvolvedora web."),
    Candidato("Eduardo Nunes", ["C#", ".NET", "SQL Server"], "Engenharia da Computação", "SP", 4, "2025-06-01", "Experiência em sistemas corporativos."),
    Candidato("Fernanda Dias", ["Python", "Pandas", "Machine Learning"], "Estatística", "RS", 6, "2025-05-29", "Data scientist com foco em IA."),
]


# Função de busca com filtros
def buscar_candidatos(
    candidatos: List[Candidato],
    requisitos: Optional[List[str]] = None,
    formacao: Optional[str] = None,
    localizacao: Optional[str] = None,
    experiencia_min: int = 0,
    palavra_chave: Optional[str] = None
):
    if requisitos is None:
        requisitos = []

    requisitos = [r.lower() for r in requisitos]
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


# Função de ordenação com múltiplos critérios
def ordenar_candidatos(
    candidatos: List[Candidato],
    criterios: List[str],
    requisitos: Optional[List[str]] = None
):
    if requisitos is None:
        requisitos = []

    requisitos = [r.lower() for r in requisitos]

    def chave(c: Candidato):
        valores = []
        for crit in criterios:
            if crit == "experiencia":
                valores.append(-c.experiencia)
            elif crit == "data":
                valores.append(c.data_candidatura)
            elif crit == "score":
                valores.append(-c.score_adequacao(requisitos))
            elif crit == "relevancia":
                valores.append(-c.match_relevancia(requisitos))
        return tuple(valores)

    return sorted(candidatos, key=chave)


# Exemplo de uso
if __name__ == "__main__":
    requisitos_vaga = ["Python", "SQL"]

    print("--- Candidatos encontrados ---")
    filtrados = buscar_candidatos(candidatos, requisitos=requisitos_vaga, localizacao="SP")
    for c in filtrados:
        print(c)

    print("\n--- Ordenados por score de adequação e data ---")
    ordenados = ordenar_candidatos(filtrados, criterios=["score", "data"], requisitos=requisitos_vaga)
    for c in ordenados:
        print(str(c))

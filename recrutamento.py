import unicodedata
from datetime import datetime, timedelta
from typing import List, Optional
from collections import Counter
import random # Necessário para a fábrica de dados

# --- FERRAMENTAS PARA A FÁBRICA DE DADOS (NOVO) ---

NOMES_MASC = ["Gabriel", "Lucas", "Matheus", "Rafael", "Gustavo", "Enzo", "Felipe", "João", "Pedro", "Arthur", "Heitor", "Bernardo"]
NOMES_FEM = ["Julia", "Sofia", "Isabella", "Maria", "Laura", "Alice", "Valentina", "Helena", "Manuela", "Lívia", "Mariana", "Beatriz"]
SOBRENOMES = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira", "Lima", "Gomes", "Ribeiro", "Martins"]
LOCALIZACOES = ["SP", "RJ", "MG", "RS", "PR", "SC", "BA", "CE", "DF", "GO", "PE", "ES"]

SKILLS_POR_FORMACAO = {
    "Engenharia de Software": ["testes automatizados", "ci/cd", "solid", "design patterns", "metodologias ageis"],
    "Ciência da Computação": ["algoritmos", "estrutura de dados", "c++", "inteligencia artificial", "compiladores"],
    "Sistemas de Informação": ["banco de dados", "uml", "requisitos", "gestao de projetos", "power bi"],
    "Engenharia da Computação": ["sistemas embarcados", "verilog", "automação industrial", "robotica", "iot"],
    "Estatística": ["teste de hipotese", "modelo de regressao", "r", "sas", "analise multivariada"],
    "Administração": ["liderança", "gestao de pessoas", "planejamento estrategico", "finanças", "marketing"],
    "Redes de Computadores": ["cisco", "firewall", "roteamento", "tcp/ip", "seguranca de redes"],
    "Design Gráfico": ["photoshop", "illustrator", "branding", "tipografia", "identidade visual"]
}

def criar_candidatos(formacao: str, quantidade: int) -> List['Candidato']:
    """Gera uma lista de candidatos aleatórios para uma dada formação."""
    novos_candidatos = []
    for _ in range(quantidade):
        # Escolhe nome e sobrenome
        nome = random.choice(NOMES_MASC + NOMES_FEM)
        sobrenome = random.choice(SOBRENOMES)
        
        # Define atributos básicos
        localizacao = random.choice(LOCALIZACOES)
        experiencia = random.randint(1, 10)
        data_candidatura = datetime.now() - timedelta(days=random.randint(1, 365))
        
        # Seleciona habilidades da área
        base_skills = SKILLS_POR_FORMACAO[formacao]
        num_skills = random.randint(2, 4)
        habilidades = random.sample(base_skills, num_skills)
        
        # Cria um resumo simples
        resumo = f"Profissional da area de {formacao} com {experiencia} anos de experiencia e conhecimento em {habilidades[0]} e {habilidades[1]}."
        
        novo_candidato = Candidato(
            nome=f"{nome} {sobrenome}",
            habilidades=habilidades,
            formacao=formacao,
            localizacao=localizacao,
            experiencia=experiencia,
            data_candidatura=data_candidatura.strftime("%Y-%m-%d"),
            resumo=resumo
        )
        novos_candidatos.append(novo_candidato)
    return novos_candidatos

# --- FUNÇÕES HELPER E CLASSE CANDIDATO (sem alterações) ---

def normalizar_string(texto: str) -> str:
    if not texto: return ""
    nfkd_form = unicodedata.normalize('NFKD', texto.lower())
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

def selecionar_opcao(titulo: str, opcoes_display: list, opcoes_reais: list) -> str:
    print(f"\n=> {titulo}:")
    if not opcoes_display:
        print("   - Nenhuma opção disponível.")
        return ""
    for i, op in enumerate(opcoes_display, 1):
        print(f"   {i} - {op}")
    escolha = input(f"Digite o nome, parte do nome, abreviação ou número (ou deixe em branco): ")
    if not escolha: return ""
    if escolha.isdigit():
        indice = int(escolha)
        if 1 <= indice <= len(opcoes_reais): return opcoes_reais[indice - 1]
        else:
            print("   (Aviso: Número inválido. O filtro será ignorado.)")
            return ""
    return escolha

MAPA_DE_TERMOS = {
    "adm": ["administracao"], "cc": ["ciencia da computacao"], "ec": ["engenharia da computacao"],
    "es": ["engenharia de software"], "si": ["sistemas de informacao"], "estat": ["estatistica"],
    "design": ["design grafico"], "redes": ["redes de computadores"],
    "dev": ["desenvolvedor", "desenvolvedora", "developer"], "desenvolvedor": ["desenvolvedor", "desenvolvedora", "developer"],
    "developer": ["desenvolvedor", "desenvolvedora", "developer"], "dados": ["dados", "data", "bi"], "data": ["dados", "data", "bi"],
    "bi": ["dados", "data", "bi"], "ia": ["ia", "inteligência artificial", "machine learning"], "ai": ["ia", "inteligência artificial", "machine learning"],
    "ml": ["ia", "inteligência artificial", "machine learning"], "analista": ["analista", "análise"], "cloud": ["cloud", "aws"],
}

class Candidato:
    def __init__(self, nome, habilidades, formacao, localizacao, experiencia, data_candidatura, resumo):
        self.nome, self.habilidades, self.formacao, self.localizacao, self.experiencia, self.resumo = nome, [h.lower() for h in habilidades], formacao, localizacao, experiencia, resumo
        try: self.data_candidatura = datetime.strptime(data_candidatura, "%Y-%m-%d")
        except ValueError: raise ValueError(f"Data inválida para {nome}. Use o formato YYYY-MM-DD.")
    def match_relevancia(self, requisitos: List[str]) -> int: return len([h for h in requisitos if normalizar_string(h) in [normalizar_string(s) for s in self.habilidades]])
    def score_adequacao(self, requisitos: List[str]) -> int: return self.match_relevancia(requisitos) * 10 + self.experiencia
    def __repr__(self): return f"{self.nome} | {self.localizacao} | {self.experiencia} anos | {self.data_candidatura.date()}"
    def __str__(self): return f"Nome: {self.nome}\nFormação: {self.formacao} ({self.localizacao})\nExperiência: {self.experiencia} anos\nHabilidades: {', '.join(self.habilidades).title()}\nCandidatura: {self.data_candidatura.date()}\nResumo: {self.resumo}\n"

# --- BASE DE DADOS EXPANDIDA ---
candidatos_originais = [
    Candidato("Ana Souza", ["python", "sql", "git"], "Engenharia de Software", "SP", 3, "2024-06-01", "Trabalhou com análise de dados e automação de planilhas."),
    Candidato("Carlos Lima", ["java", "spring", "aws"], "Ciência da Computação", "RJ", 5, "2024-05-30", "Desenvolvedor backend focado em microserviços e Cloud."),
    Candidato("Beatriz Rocha", ["python", "django", "html"], "Sistemas de Informação", "MG", 2, "2024-06-02", "Desenvolvedora web full-stack com projetos em Django."),
    Candidato("Eduardo Nunes", ["c#", ".net", "sql server"], "Engenharia da Computação", "SP", 4, "2024-06-01", "Experiência em sistemas corporativos e manutenção de legados."),
    Candidato("Fernanda Dias", ["python", "pandas", "machine learning"], "Estatística", "RS", 6, "2023-11-20", "Data scientist com foco em IA e modelos preditivos."),
    Candidato("Lucas Mendes", ["python", "sql", "tableau"], "Administração", "SP", 4, "2024-05-15", "Analista de BI com foco em visualização de dados e dashboards."),
    Candidato("Mariana Costa", ["python", "excel", "power bi", "sql"], "Administração", "SP", 1, "2025-06-05", "Recém-formada com foco em análise de dados e business intelligence."),
    Candidato("Ricardo Alves", ["java", "kotlin", "docker", "kubernetes", "aws"], "Ciência da Computação", "SC", 8, "2025-05-20", "Arquiteto de software com vasta experiência em Java e ecossistema cloud native."),
    Candidato("Juliana Pereira", ["javascript", "react", "typescript", "html", "css"], "Sistemas de Informação", "MG", 4, "2025-06-01", "Desenvolvedora Frontend com foco em React e na criação de interfaces reativas."),
    Candidato("Thiago Martins", ["c#", ".net", "sql"], "Engenharia da Computação", "PR", 2, "2025-06-03", "Desenvolvedor .NET júnior com interesse em sistemas distribuídos."),
    Candidato("Camila Ramos", ["terraform", "ansible", "docker", "aws", "python"], "Redes de Computadores", "SP", 5, "2025-04-30", "Engenheira DevOps especializada em automação de infraestrutura como código (IaC)."),
    Candidato("Felipe Nobre", ["figma", "adobe xd", "ux research"], "Design Gráfico", "RJ", 6, "2025-05-25", "Designer de produto com foco em experiência do usuário e prototipação de interfaces."),
]

# Gera os novos candidatos e os adiciona à lista
candidatos = candidatos_originais[:]
formacoes_existentes = list(SKILLS_POR_FORMACAO.keys())
for formacao in formacoes_existentes:
    candidatos.extend(criar_candidatos(formacao, 5))


def ordenar_candidatos(lista_de_candidatos, criterios, requisitos=None):
    if requisitos is None: requisitos = []
    def chave_de_ordenacao(c):
        valores = []
        for crit in criterios:
            if crit == "experiencia": valores.append(-c.experiencia)
            elif crit == "data": valores.append(-c.data_candidatura.timestamp())
            elif crit == "score": valores.append(-c.score_adequacao(requisitos))
            elif crit == "relevancia": valores.append(-c.match_relevancia(requisitos))
        return tuple(valores)
    return sorted(lista_de_candidatos, key=chave_de_ordenacao)

def filtro_em_cascata():
    print("--- Plataforma de Recrutamento: Filtro em Cascata ---")
    mapa_formacao_reverso = {}
    formacao_abbrs = ["adm", "cc", "ec", "es", "si", "estat", "design", "redes"]
    for abbr in formacao_abbrs:
        nome_completo_norm = MAPA_DE_TERMOS.get(abbr, [""])[0]
        if nome_completo_norm: mapa_formacao_reverso[nome_completo_norm] = abbr
    while True:
        candidatos_filtrados = candidatos[:]
        filtros_aplicados = {}
        requisitos = []
        try:
            print("\n--- Nova Busca ---")
            contagem = Counter(c.formacao for c in candidatos_filtrados)
            opcoes_reais = sorted(list(contagem.keys()))
            opcoes_display = []
            for formacao in opcoes_reais:
                abbr = mapa_formacao_reverso.get(normalizar_string(formacao))
                texto_cand = "candidato" if contagem[formacao] == 1 else "candidatos"
                display = f"{formacao} {'('+abbr+') ' if abbr else ''}[{contagem[formacao]} {texto_cand}]"
                opcoes_display.append(display)
            escolha = selecionar_opcao("Opções de Formação", opcoes_display, opcoes_reais)
            if escolha:
                filtros_aplicados['Formação'] = escolha
                escolha_normalizada = normalizar_string(escolha)
                termos_busca = MAPA_DE_TERMOS.get(escolha_normalizada, [escolha_normalizada])
                candidatos_filtrados = [c for c in candidatos_filtrados if any(termo in normalizar_string(c.formacao) for termo in termos_busca)]
                if not candidatos_filtrados: raise ValueError(f"Nenhum candidato encontrado para a formação '{escolha}'.")
            if candidatos_filtrados:
                contagem = Counter(h for c in candidatos_filtrados for h in c.habilidades)
                opcoes_reais = sorted(list(contagem.keys()))
                opcoes_display = [f"{h} [{contagem[h]} {'cand.' if contagem[h] == 1 else 'cands.'}]" for h in opcoes_reais]
                escolha = selecionar_opcao("Habilidades disponíveis no grupo", opcoes_display, opcoes_reais)
                if escolha:
                    requisitos = [h.strip() for h in escolha.split(',')]
                    reqs_norm = [normalizar_string(h) for h in requisitos]
                    candidatos_com_habilidade = [c for c in candidatos_filtrados if any(r in [normalizar_string(h) for h in c.habilidades] for r in reqs_norm)]
                    if not candidatos_com_habilidade:
                        print(f"\nAVISO: Nenhum candidato com os filtros ({filtros_aplicados}) possui a(s) habilidade(s) '{', '.join(requisitos)}'.")
                        for habilidade in requisitos:
                            hab_norm = normalizar_string(habilidade)
                            onde_tem = sorted(list(set(c.formacao for c in candidatos if hab_norm in [normalizar_string(h_cand) for h_cand in c.habilidades])))
                            if onde_tem: print(f"  -> A habilidade '{habilidade}' foi encontrada em: {', '.join(onde_tem)}.")
                        raise ValueError("Busca interrompida pela falta de habilidades.")
                    candidatos_filtrados = candidatos_com_habilidade
            if not candidatos_filtrados:
                 print("\nNenhum candidato corresponde a todos os filtros.")
            else:
                print("\n--- Candidatos Encontrados (Pré-visualização) ---")
                for i, c in enumerate(candidatos_filtrados, 1):
                    relevancia = c.match_relevancia(requisitos)
                    score = c.score_adequacao(requisitos)
                    info_str = (f"{i}. {c.nome:<20} | Relevância: {relevancia:<2} | Score: {score:<3} | Exp: {c.experiencia}a | Data: {c.data_candidatura.date()}")
                    print(info_str)
                print(f"\nForam encontrados {len(candidatos_filtrados)} candidato(s).")
                CRITERIOS_VALIDOS = ["relevancia", "score", "experiencia", "data"]
                while True:
                    print("\nComo deseja ordenar os resultados? (pode escolher vários, ex: 1, 4)")
                    for i, crit in enumerate(CRITERIOS_VALIDOS, 1): print(f"   {i} - {crit}")
                    ordem_input = input("=> Critérios (padrão: score, experiencia): ")
                    if not ordem_input:
                        criterios_ordem = ["score", "experiencia"]
                    else:
                        partes = [p.strip().lower() for p in ordem_input.split(',')]
                        criterios_ordem = []
                        for parte in partes:
                            if parte.isdigit() and 1 <= int(parte) <= len(CRITERIOS_VALIDOS):
                                criterios_ordem.append(CRITERIOS_VALIDOS[int(parte) - 1])
                            else:
                                criterios_ordem.append(parte)
                    if all(c in CRITERIOS_VALIDOS for c in criterios_ordem): break
                    else: print("   (Erro: Um ou mais critérios são inválidos. Tente novamente.)")
                candidatos_ordenados = ordenar_candidatos(candidatos_filtrados, criterios_ordem, requisitos)
                print("\n--- Resultado da Busca Ordenado ---")
                for i, c in enumerate(candidatos_ordenados, 1):
                    print(f"--- {i}º LUGAR ---")
                    print(str(c))
        except ValueError as e:
            print(f"\n[Busca Finalizada] Motivo: {e}")
        continuar = input("\nDeseja fazer uma nova busca? (S/n): ").lower()
        if continuar == 'n':
            print("\nEncerrando a plataforma. Até logo!")
            break

if __name__ == "__main__":
    filtro_em_cascata()

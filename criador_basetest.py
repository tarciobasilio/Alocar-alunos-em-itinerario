import pandas as pd
import random
from datetime import datetime

# 1. CONFIGURAÇÃO DOS DADOS
# Lista exata dos itinerários que seu código espera (para o IF funcionar)
lista_itinerarios = [
    "Tramas temporais: entre histórias e palavras",
    "Revoluções, Transformações e Descobertas",
    "Palavrar: análise e interpretação textual para o sucesso no vestibular",
    "Arquitetura Sustentável e Espaço Urbano: desenvolvendo um projeto maker",
    "Ficção científica: entre palavras, lógicas e partículas",
    "Iniciação Científica",
    "Sociedade brasileira e autoritarismo"
]

# Dados para gerar aleatoriedade
nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia", "Lucas", "Mariana", "Nicolas", "Olivia", "Pedro", "Rafael", "Sofia", "Thiago", "Vitoria", "Wesley"]
sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira", "Lima", "Gomes", "Costa", "Ribeiro", "Martins"]
turmas = ["3º A", "3º B", "3º C", "3º D"]

quantidade_alunos = 250 # Vamos gerar bastante gente para testar a lotação das turmas

dados_falsos = []

print("Gerando dados falsos...")

# 2. LOOP DE GERAÇÃO
for i in range(quantidade_alunos):
    # Escolhe nome e sobrenome aleatórios
    nome_completo = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
    email = f"{nome_completo.lower().replace(' ', '.')}@escola.com"
    turma = random.choice(turmas)
    
    # IMPORTANTE: Escolhe 3 itinerários DIFERENTES aleatoriamente (sample não repete itens)
    escolhas = random.sample(lista_itinerarios, 3)
    
    # Monta a linha conforme as colunas que seu código pediu
    linha = {
        "Carimbo de data/hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "Endereço de e-mail": email,
        "Nome Completo (sem abreviaturas)": nome_completo,
        "Qual a sua turma?": turma,
        "1ª OPÇÃO - Dentre as opções abaixo, escolha um itinerário": escolhas[0],
        "2ª OPÇÃO - Escolha um itinerário, DIFERENTE do anterior.": escolhas[1],
        "3ª OPÇÃO": escolhas[2]
    }
    dados_falsos.append(linha)

# 3. CRIAÇÃO DO DATAFRAME
df = pd.DataFrame(dados_falsos)

# 4. SALVANDO EM EXCEL
# O nome da aba (sheet_name) deve ser exatamente o que está no seu código de leitura
nome_arquivo = "teste_alunos.xlsx"
df.to_excel(nome_arquivo, index=False, sheet_name="Respostas ao formulário 1")

print(f"Sucesso! Arquivo '{nome_arquivo}' criado com {quantidade_alunos} alunos.")
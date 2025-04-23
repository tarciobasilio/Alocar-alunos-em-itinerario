'''
#Antes de tudo rode no prompt de comando os seguintes códigos:
#Pesquise 'cmd' na pesquisa do windows e abra o prompt de comando, depois digite:
pip install numpy
pip install pandas
pip install openpyxl
pip install xlsxwriter
'''

import pandas as pd
import numpy as np


df = pd.read_excel("C:/Users/francisco_viana/Downloads/INSCRIÇÃO QUARTA ITINERÁRIO TEMÁTICO 1º SEM 2024 (respostas).xlsx", sheet_name = "Respostas ao formulário 1") #mudar esse caminho
base = np.array(df)
#print(base)


'''
Veja se nessa base tem:
0 - Carimbo de data/hora	
1 - Endereço de e-mail	
2 - Nome Completo (sem abreviaturas)	
3 - Qual a sua turma?	
3 - 1ª OPÇÃO - Dentre as opções abaixo, escolha um itinerário	
5 - 2ª OPÇÃO - Escolha um itinerário, DIFERENTE do anterior.
6 - 3ª OPÇÃO

Se for o arquivo4a com somente o nome "MATRIZ" e aba "respostas do formulário" não deve existir a coluna índice , portanto as colunas tem índice diminuído em 1.
'''


#Nome dos itinerários
itinerarioA = "Tramas temporais: entre histórias e palavras (Luciana e Edney)"
itinerarioB = "Revoluções, Transformações e Descobertas (Francisco e Edney)"
itinerarioC = "Palavrar: análise e interpretação textual para o sucesso no vestibular (Kátia)"
itinerarioD = "Arquitetura Sustentável e Espaço Urbano: desenvolvendo um projeto maker (Fábio)"
itinerarioE = "Ficção científica: entre palavras, lógicas e partículas (Francisco e Luciana)"
itinerarioF = "Iniciação Científica (Homero)"
itinerarioG = "Sociedade brasileira e autoritarismo (Graziano)"


#Quantidade de alunos por turma
limite_alunos = 33 # Na verdade significa +1 , porque no Python a gente conta o zero


#Gerando o arquivo4a onde teremos as informações aluno por aluno
#Ou seja, em que itinerário cada aluno entrou
arquivo4a = open('arquivo4a.txt', 'w')


tamanho = len(base)

profA = [] #mudar nomes aqui usar o CTRL+H 
profB = [] #mudar nomes aqui
profC = [] #mudar nomes aqui 
profD = [] #mudar nomes aqui 
profE = [] #mudar nomes aqui 
profF = []  #               
profG = []  #                
    

for i in range(tamanho): 	#também precisa mudar os nomes abaixo de acordo com o que está na planilha - ctrl+H 
    if base[i][4] == itinerarioA and len(profA) <= limite_alunos:
        profA.append(base[i])
        print(base[i][2], " - Entrou na primeira opção", file=arquivo4a)
    elif base[i][4] == itinerarioB and len(profB) <= limite_alunos:
        profB.append(base[i])
        print(base[i][2], " - Entrou na primeira opção", file=arquivo4a)
    elif base[i][4] == itinerarioE and len(profC) <= limite_alunos:
        profC.append(base[i])
        print(base[i][2], " - Entrou na primeira opção", file=arquivo4a)
    elif base[i][4] == itinerarioC and len(profD) <= limite_alunos:
        profD.append(base[i])
        print(base[i][2], " - Entrou na primeira opção", file=arquivo4a)
    elif base[i][4] == itinerarioD and len(profE) <= limite_alunos:
        profE.append(base[i])
        print(base[i][2], " - Entrou na primeira opção", file=arquivo4a)
    elif base[i][4] == itinerarioF and len(profF) <= limite_alunos:
        profF.append(base[i])
        print(base[i][2], " - Entrou na primeira opção", file=arquivo4a)
    elif base[i][4] == itinerarioG and len(profG) <= limite_alunos:
        profG.append(base[i])
        print(base[i][2], " - Entrou na primeira opção", file=arquivo4a)
    else:

        if base[i][5] == itinerarioA and len(profA) <= limite_alunos:
            profA.append(base[i])
        elif base[i][5] == itinerarioB and len(profB) <= limite_alunos:
            profB.append(base[i])
            print(base[i][2], " - Entrou na segunda opção", file=arquivo4a)
        elif base[i][5] == itinerarioC and len(profD) <= limite_alunos:
            profD.append(base[i])
            print(base[i][2], " - Entrou na segunda opção", file=arquivo4a)
        elif base[i][5] == itinerarioD and len(profE) <= limite_alunos:
            profE.append(base[i])
            print(base[i][2], " - Entrou na segunda opção", file=arquivo4a)
        elif base[i][5] == itinerarioF and len(profF) <= limite_alunos:
            profF.append(base[i])
            print(base[i][2], " - Entrou na segunda opção", file=arquivo4a)
        elif base[i][5] == itinerarioE and len(profC) <= limite_alunos:
            profC.append(base[i])
            print(base[i][2], " - Entrou na segunda opção", file=arquivo4a)
        elif base[i][5] == itinerarioG and len(profG) <= limite_alunos:
            profG.append(base[i])
            print(base[i][2], " - Entrou na segunda opção", file=arquivo4a)

        else:
            if base[i][6] == itinerarioA and len(profA) <= limite_alunos:
                profA.append(base[i])
                print(base[i][2], " - Entrou na terceira opção", file=arquivo4a)
            elif base[i][6] == itinerarioB and len(profB) <= limite_alunos:
                profB.append(base[i])
                print(base[i][2], " - Entrou na terceira opção", file=arquivo4a)
            elif base[i][6] == itinerarioC and len(profD) <= limite_alunos:
                profD.append(base[i])
                print(base[i][2], " - Entrou na terceira opção", file=arquivo4a)
            elif base[i][6] == itinerarioD and len(profE) <= limite_alunos:
                profE.append(base[i])
                print(base[i][2], " - Entrou na terceira opção", file=arquivo4a)
            elif base[i][6] == itinerarioF and len(profF) <= limite_alunos:
                profF.append(base[i])
                print(base[i][2], " - Entrou na terceira opção", file=arquivo4a)
            elif base[i][6] == itinerarioE and len(profC) <= limite_alunos:
                profC.append(base[i])
                print(base[i][2], " - Entrou na terceira opção", file=arquivo4a)
            elif base[i][6] == itinerarioG and len(profG) <= limite_alunos:
                profG.append(base[i])
                print(base[i][2], " - Entrou na terceira opção", file=arquivo4a)


            else:
                print("\n\n\n ", base[i][2], " - Precisa de quarta opção\n\n\n", file=arquivo4a)


arquivo4a.close() #fechando o arquivo4a dos dados aluno por aluno


# Usando o ExcelWriter, cria um doc .xlsx, usando engine='xlsxwriter'
writer = pd.ExcelWriter('itineras4a.xlsx', engine='xlsxwriter')

# Armazena cada df em uma planilha diferente do mesmo arquivo4a
pd.DataFrame(profA).to_excel(writer, sheet_name='profA')
pd.DataFrame(profB).to_excel(writer, sheet_name='profB')
pd.DataFrame(profD).to_excel(writer, sheet_name='profD')
pd.DataFrame(profE).to_excel(writer, sheet_name='profE')
pd.DataFrame(profC).to_excel(writer, sheet_name='profC')
pd.DataFrame(profF).to_excel(writer, sheet_name='profF')
pd.DataFrame(profG).to_excel(writer, sheet_name='profG')


# Fecha o ExcelWriter e gera o arquivo4a .xlsx
writer._save()    


print("Programa finalizado com sucesso!")

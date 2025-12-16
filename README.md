📚 Alocação Automática de Alunos em Optativas


🎯 Visão Geral do Projeto: Automação para Otimização Logística

Este projeto é um Case Study real de Otimização de Processos (ETL) desenvolvido durante minha atuação como Professor Assistente de Matemática. Ele demonstra minha capacidade de identificar gargalos operacionais e aplicar o Raciocínio Lógico/Computacional para gerar valor imediato, transformando dias de trabalho em minutos.

Produto: Script em Python que aloca alunos em disciplinas optativas, respeitando a ordem de preferência e a capacidade máxima das turmas.
Tecnologias: Python (Pandas), Excel/CSV.


📜 A História e o Problema de Negócio (O "Porquê" do Projeto)

O Gargalo (O Processo Manual):
O Colégio precisava alocar anualmente centenas de alunos em diversas disciplinas optativas com capacidade limitada. O processo era:

1. Reunir a equipe em uma sala (vários computadores, várias pessoas).
2. Abrir a grande planilha de controle (Excel).
3. Um colaborador lia o nome do aluno e sua 1ª opção.
4. Outro verificava na planilha se a optativa tinha vaga.
5. Se tivesse, a opção era marcada na planilha (o que gerava risco de sobrescrita e erro humano).
6. Se não tivesse, o aluno passava para a 2ª opção, repetindo o ciclo.

Esse trabalho braçal e minucioso exigia 3 a 4 dias inteiros de trabalho da equipe pedagógica, além de gerar estresse e alto risco de erros de alocação.

A Solução (O Impacto da Automação):
Ao aplicar o Raciocínio Computacional à lógica do problema, criei um script simples em Python que simula e executa a alocação em segundos:

Antes (Processo Manual)
Risco alto de erro humano
3 a 4 dias de trabalho exaustivo
Prioridade e capacidade complexas
Ocupação de 4 pessoas por dias

Depois (Processo Automatizado)
Risco zero de erro de alocação
1 tarde de desenvolvimento e 5 segundos de execução
Lógica de if/else transparente e auditável
Ocupação de 3 (ou menos) pessoas por somente uma tarde

O script transforma a planilha de entrada (bruta) em um resultado final auditável e instantâneo.


💻 Estrutura do Projeto e Principais Etapas

1o momento:
No trabalho original os alunos respondiam um forms, que servia como base de dados para o projeto inicial, porém conforme quis continuar o projeto mesmo após sair da empresa criei um código que gera uma planilha para que eu pudesse continuar melhorias no código.
A ideia inicial foi ler cada linha da tabela provinda do forms e verificar através de diversos if/elif aninhados se o itinerário estava disponível. Com isso, alocar o aluno e em seguida printar a opção em que o aluno entrou.
O projeto gera um arquivo .txt informando em que opção o aluno entrou, ou se será necessário chamar o aluno para escolher uma quarta opção. Também gera um .xlsx mostrando como as turmas de cada professor/itinerário ficou.

2o momento:
Ao revisitar o código decidir manter o arquivo original intacto, até como uma espécie de respeito ao momento que vivi. Criei um arquivo novo para fazer as modificações que eu gostaria de implementar.
Para poder melhorar o código pedi ajuda para uma IA criar uma base fictícia para que eu pudesse treinar a execução do código.
Nesse momento segui dicas de por um fim à "Muralha de Ifs/Elifs" usando Dicionário e iterando sobre ele. Para isso também foi necessário criar algumas novas variáveis úteis.


📁 Arquivos:

arquivo4a.txt: txt dizendo a opção que cada aluno escolheu
itineras4a.xlsx: excel contendo em cada aba como ficou cada turma pro itinerário
criador_basetest.py: código para gerar bases de treinamento para o código
teste_alunos.xlsx: base criada pelo código python acima que serve como base para o código


🚀 Próximos Passos e Oportunidades de Evolução

O projeto em sua versão atual resolve o gargalo primário (a alocação em si). Apesar disso existem oportunidades de evolução (e que pretendo implementar em breve), que seriam:

1. Acesso por Nome de Coluna (Substituindo os Índices [i][4]) - Manter o objeto como DataFrame do Pandas. Não converter para array.
2. Unificar nomes para que eu possa usar o nome do itinerário na base como chave do dicionário - o que pode me gerar menos loops e economizar linhas de código.
3. Otimizar diminuindo loops - Tentar fazer tudo usando um loop único sem usar um loop pra cada opção

Caso tenha ideias sou todo ouvidos.



Desenvolvido por Tárcio Basílio | Bacharel em Matemática Aplicada e Computacional (USP).

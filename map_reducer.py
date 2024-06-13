"""

Trabalho apresentado para disciplina de Modelagem MapReduce
Pelos alunos:

- Debora de Oliveira Lima
- Leonardo J F de Abreu Júnior
- Patrick Vieira
- Bruno Leonardo Santos Menezes

Descrição
○ Desenvolver uma versão do contador de palavras
(Wordcount) para o documento “Beyond Good and Evil”, de
Friedrich Nietzsche usando os conceitos de MapReduce
apresentados em nossas aulas

Ferramentas a serem empregadas
○ O trabalho deve ser inteiramente desenvolvido em Python
(preferencialmente Python 3)

Input
○ Arquivo TXT disponível no Moodle no material da disciplina

Detalhamento
○ Função mapper: Recebe um único nome de arquivo e retorna
uma sequência de tuplas (palavra, 1)
○ Função partitioner: Recebe como entrada os tuplas do
mapper e gera uma saída uma lista de tuplas contendo as
palavras e uma lista: [('BigData', [1,1] ), ('map', [1,1,1])]
○ Função reducer: Recebe a tupla ('BigData', [1,1]) e saída:
(palavra, #ocorrências)

Prazo de entrega: 17/06/2024

"""


def mapeador(nome_arquivo):
    """
    
    Args:
        nome_arquivo (str): O caminho do arquivo de texto a ser lido.
        
    Returns:
        list: Uma lista de tuplas no formato (palavra, 1).
    """
    
    tuplas_palavras = []
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            palavras = linha.strip().split()
            for palavra in palavras:
                tuplas_palavras.append((palavra, 1))
    return tuplas_palavras

def particionador(tuplas_palavras):
    """
    Args:
        tuplas_palavras (list): Uma lista de tuplas no formato (palavra, 1).
        
    Returns:
        list: Uma lista de tuplas contendo as palavras e suas contagens em listas.
    """
    
    dados_particionados = {}
    for palavra, contagem in tuplas_palavras:
        if palavra in dados_particionados:
            dados_particionados[palavra].append(contagem)
        else:
            dados_particionados[palavra] = [contagem]
    
    return list(dados_particionados.items())

def redutor(dados_particionados):
    """
    Args:
        dados_particionados (list): Uma lista de tuplas no formato ('palavra', [1, 1, ...]).
    
    Returns:
        list: Uma lista de tuplas no formato ('palavra', contagem_ocorrencias).
    """
    
    dados_reduzidos = []
    for palavra, contagens in dados_particionados:
        total_contagem = sum(contagens)
        dados_reduzidos.append((palavra, total_contagem))
    
    return dados_reduzidos

file = 'Beyond Good and Evil - Friedrich Nietzsche.txt'

mapper = mapeador(file)
partitioner = particionador(mapper)
reducer = redutor(partitioner)

print(reducer)

output_file = 'output.txt'

with open(output_file, 'w', encoding='utf-8') as output:
    for palavra, contagem in reducer:
        output.write(f'{palavra}: {contagem}\n')
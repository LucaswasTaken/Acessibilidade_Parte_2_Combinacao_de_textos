import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize


#Função de recursão. Pega a primeira palavra e combina ou separa em relacao ao
#resto da frade, recursivamente.

def recursao_combinacao(frase):
  if(len(frase)==1):
    return frase

  palavra_inicial = frase[0]
  ultimas_palavras = frase[1:]

  combinacoes_das_ultimas_palavras = recursao_combinacao(ultimas_palavras)

  combinador = ' '
  separador = ','
  separados = []
  combinados = []

  for combinacao in combinacoes_das_ultimas_palavras:
    combinados.append(combinador.join([palavra_inicial,combinacao]))
    separados.append(separador.join([palavra_inicial,combinacao]))
  return combinados + separados

text = input('Digite o texto: ')

token_text = word_tokenize(text)

print(recursao_combinacao(token_text))